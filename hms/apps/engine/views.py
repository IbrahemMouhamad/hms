# Copyright (C) 2021 Ibrahem Mouhamad


from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated

from hms.apps.engine import models
from hms.apps.engine.serializers import (
    HospitalSerializer, DepartmentSerializer, StaffSerializer, DoctorSerializer, NurseSerializer, PatientSerializer,
    DiagnosisSerializer, ExaminationSerializer, PrescriptionSerializer, TreatmentSerializer, EmployeeSerializer,
    AppointmentSerializer
)

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of hospital according to query parameters (12 hospitals per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this hospital",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new hospital'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific hospital'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific hospital'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a hospital'))
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = models.Hospital.objects.all().order_by('-id')
    search_fields = ("name", "address")
    ordering_fields = ("id", "name")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return HospitalSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of department according to query parameters (12 departments per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this department",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new department'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific department'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific department'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a department'))
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all().order_by('-id')
    search_fields = ("name", "hospital_id")
    ordering_fields = ("id", "name")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return DepartmentSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of staff according to query parameters (12 staffs per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this staff",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new staff'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific staff'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific staff'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a staff'))
class StaffViewSet(viewsets.ModelViewSet):
    queryset = models.Staff.objects.all().order_by('-id')
    search_fields = ("name", "department_id", "type")
    ordering_fields = ("id", "name")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return StaffSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of doctors according to query parameters (12 doctors per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this doctor",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new doctor'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific doctor'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific doctor'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a doctor'))
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all().order_by('-id')
    search_fields = ("speciality")
    ordering_fields = ("id", "speciality")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return DoctorSerializer

    def get_permissions(self):
        permissions = []

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of nurses according to query parameters (12 nurses per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this nurse",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new nurse'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific nurse'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific nurse'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a nurse'))
class NurseViewSet(viewsets.ModelViewSet):
    queryset = models.Nurse.objects.all().order_by('-id')
    search_fields = ("degree")
    ordering_fields = ("id", "degree")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return NurseSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of patients according to query parameters (12 patients per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this patient",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new patient'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific patient'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific patient'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a patient'))
class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all().order_by('-id')
    search_fields = ("accepted_date")
    ordering_fields = ("id", "accepted_date")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return PatientSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of diagnosis according to query parameters (12 diagnosis per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this diagnosis",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new diagnosis'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific diagnosis'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific diagnosis'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a diagnosis'))
class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = models.Diagnosis.objects.all().order_by('-id')
    search_fields = ("name")
    ordering_fields = ("id", "name")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return DiagnosisSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of examinations according to query parameters (12 examinations per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this examination",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new examination'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific examination'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific examination'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a examination'))
class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = models.Examination.objects.all().order_by('-id')
    search_fields = ("type", "name")
    ordering_fields = ("id", "name")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return ExaminationSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of prescriptions according to query parameters (12 prescriptions per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this prescription",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new prescription'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific prescription'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific prescription'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a prescription'))
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = models.Prescription.objects.all().order_by('-id')
    search_fields = ("name")
    ordering_fields = ("id", "name")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return PrescriptionSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of treatments according to query parameters (12 treatments per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this treatment",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new treatment'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific treatment'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific treatment'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a treatment'))
class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = models.Treatment.objects.all().order_by('-id')
    search_fields = ("type", "name")
    ordering_fields = ("id", "name")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return TreatmentSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of employees according to query parameters (12 employees per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this employee",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new employee'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific employee'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific employee'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a employee'))
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all().order_by('-id')
    search_fields = ("type")
    ordering_fields = ("id", "type")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return EmployeeSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Returns a paginated list of appointments according to query parameters (12 appointments per page)',
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="A unique number value identifying this appointment",
            type=openapi.TYPE_NUMBER),
    ])
)
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='Method creates a new appointment'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='Method returns details of a specific appointment'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='Method deletes a specific appointment'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='Methods does a partial update of chosen fields in a appointment'))
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all().order_by('-id')
    search_fields = ("date", "room_number")
    ordering_fields = ("id", "date", "room_number")
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_serializer_class(self):
        return AppointmentSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [perm() for perm in permissions]
