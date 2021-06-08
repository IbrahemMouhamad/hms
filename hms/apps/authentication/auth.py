# Copyright (C) 2021 Ibrahem Mouhamad

from django.conf import settings
from django.db.models import Q
import rules
from . import AUTH_ROLE
from rest_framework.permissions import BasePermission
from django.core import signing
from rest_framework.authentication import TokenAuthentication as _TokenAuthentication
from django.contrib.auth import login

# Even with token authorization it is very important to have a valid session id
# in cookies because in some cases we cannot use token authorization (e.g. when
# we redirect to the server in UI using just URL). To overkill that we override
# the class to call `login` method which restores the session id in cookies.
class TokenAuthentication(_TokenAuthentication):
    def authenticate(self, request):
        auth = super().authenticate(request)
        session = getattr(request, 'session')
        if auth is not None and session.session_key is None:
            login(request, auth[0], 'django.contrib.auth.backends.ModelBackend')
        return auth

def register_signals():
    from django.db.models.signals import post_migrate, post_save, pre_save
    from django.contrib.auth.models import User, Group

    def create_groups(sender, **kwargs):
        for role in AUTH_ROLE:
            db_group, _ = Group.objects.get_or_create(name=role)
            db_group.save()

    post_migrate.connect(create_groups, weak=False)

    if settings.DJANGO_AUTH_TYPE == 'BASIC':
        from .auth_basic import create_user

        post_save.connect(create_user, sender=User)

# AUTH PREDICATES
has_admin_role = rules.is_group_member(str(AUTH_ROLE.ADMIN))
has_receptionist_role = rules.is_group_member(str(AUTH_ROLE.RECETIONIST))
has_doctor_role = rules.is_group_member(str(AUTH_ROLE.DOCTOR))
has_nurse_role = rules.is_group_member(str(AUTH_ROLE.NURSE))
has_user_role = rules.is_group_member(str(AUTH_ROLE.USER))

# AUTH PERMISSIONS RULES
rules.add_perm('engine.role.user', has_user_role)
rules.add_perm('engine.role.receptionist', has_receptionist_role)
rules.add_perm('engine.role.doctor', has_doctor_role)
rules.add_perm('engine.role.nurse', has_nurse_role)
rules.add_perm('engine.role.admin', has_admin_role)

class AdminRolePermission(BasePermission):
    # pylint: disable=no-self-use
    def has_permission(self, request, view):
        return request.user.has_perm('engine.role.admin')

class UserRolePermission(BasePermission):
    # pylint: disable=no-self-use
    def has_permission(self, request, view):
        return request.user.has_perm('engine.role.user')

class ReceptionistRolePermission(BasePermission):
    # pylint: disable=no-self-use
    def has_permission(self, request, view):
        return request.user.has_perm('engine.role.receptionist')

class DoctorRolePermission(BasePermission):
    # pylint: disable=no-self-use
    def has_permission(self, request, view):
        return request.user.has_perm('engine.role.doctor')

class nurseRolePermission(BasePermission):
    # pylint: disable=no-self-use
    def has_permission(self, request, view):
        return request.user.has_perm('engine.role.nurse')