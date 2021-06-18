# Copyright (C) 2021 Ibrahem Mouhamad


from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated

from hms.apps.engine.models import Doctor
from hms.apps.engine.serializers import DoctorSerializer

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of doctors according to query parameters (12 doctors per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this doctors",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new doctor'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific doctor'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific doctor'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a doctor'))
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('-id')
    search_fields = ("speciality")
    ordering_fields = ("id", "speciality")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return DoctorSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]