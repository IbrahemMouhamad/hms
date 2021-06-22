# Copyright (C) 2021 Ibrahem Mouhamad

from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import (
    Hospital, Department, Staff, Person, Doctor, Nurse, Patient, Diagnosis, Examination, Prescription, Treatment,
    Employee, Appointment
)

class BasicUserSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if hasattr(self, 'initial_data'):
            unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
            if unknown_keys:
                if set(['is_staff', 'is_superuser', 'groups']) & unknown_keys:
                    message = 'You do not have permissions to access some of' + \
                        ' these fields: {}'.format(unknown_keys)
                else:
                    message = 'Got unknown fields: {}'.format(unknown_keys)
                raise serializers.ValidationError(message)
        return data

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name')
        ordering = ['-id']

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True,
        slug_field='name', queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email',
            'groups', 'is_staff', 'is_superuser', 'is_active', 'last_login',
            'date_joined')
        read_only_fields = ('last_login', 'date_joined')
        write_only_fields = ('password', )
        ordering = ['-id']

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'address', 'phone_number', 'created_date', 'updated_date')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'hospital', 'created_date', 'updated_date')

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'type', 'name', 'speciality', 'department', 'created_date', 'updated_date')

class PersonSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(allow_null=True, required=False)

    class Meta:
        model = Person
        fields = ('id', 'user', 'gender', 'birth_date', 'address', 'phone_number', 'created_date', 'updated_date')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'person', 'speciality', 'is_surgeon', 'staff', 'created_date', 'updated_date')

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ('id', 'person', 'degree', 'staff', 'created_date', 'updated_date')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'person', 'accepted_date', 'sickness_history', 'allergies', 'status', 'doctor', 'created_date', 'updated_date')

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('id', 'name', 'description', 'specialist', 'created_date', 'updated_date')

class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ('id', 'type', 'name', 'cost', 'patient', 'diagnosis', 'created_date', 'updated_date')

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('id', 'name', 'description', 'patient', 'diagnosis', 'created_date', 'updated_date')

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ('id', 'type', 'name', 'description', 'cost', 'patient', 'diagnosis', 'staff', 'created_date', 'updated_date')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'type', 'person', 'staff', 'created_date', 'updated_date')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'date', 'room_number', 'patient', 'doctor', 'created_date', 'updated_date')


