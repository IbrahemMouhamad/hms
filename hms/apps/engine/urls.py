# Copyright (C) 2021 Ibrahem Mouhamad

from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import RedirectView
from django.conf import settings
from hms.apps.authentication.decorators import login_required

schema_view = get_schema_view(
   openapi.Info(
      title="HMS REST API",
      default_version='v1',
      description="REST API for Hospital Management System (HMS)",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ibragim1@tpu.ru"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)

# drf-yasg component doesn't handle correctly URL_FORMAT_OVERRIDE and
# send requests with ?format=openapi suffix instead of ?scheme=openapi.
# We map the required paramater explicitly and add it into query arguments
# on the server side.
def wrap_swagger(view):
    @login_required
    def _map_format_to_schema(request, scheme=None):
        if 'format' in request.GET:
            request.GET = request.GET.copy()
            format_alias = settings.REST_FRAMEWORK['URL_FORMAT_OVERRIDE']
            request.GET[format_alias] = request.GET['format']

        return view(request, format=scheme)

    return _map_format_to_schema

router = routers.DefaultRouter(trailing_slash=False)
router.register('doctors', views.DoctorViewSet)

urlpatterns = [
    # Entry point for a client
    path('', RedirectView.as_view(url=settings.UI_URL, permanent=True,
         query_string=True)),

    # documentation for API
    path('api/swagger<str:scheme>', wrap_swagger(
       schema_view.without_ui(cache_timeout=0)), name='schema-json'),
    path('api/swagger/', wrap_swagger(
       schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('api/docs/', wrap_swagger(
       schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),

    # entry point for API
    path('api/v1/auth/', include('hms.apps.authentication.urls')),
    path('api/v1/', include((router.urls, 'hms'), namespace='v1'))
]