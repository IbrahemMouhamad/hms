# Copyright (C) 2021 Ibrahem Mouhamad

from enum import Enum

from django.db import models

from django.contrib.auth.models import User
from phone_field import PhoneField

class GenderChoice(str, Enum):
    MALE = 'male'
    FEMALE = 'female'

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    def __str__(self):
        return self.value

class PatientStatusChoice(str, Enum):
    REGISTERED = 'male'
    WAITING = 'female'
    CHECKING = 'checking'
    ADMITED = 'admiting'
    UNDER_TEST = 'under test'
    UNDERGO_OPERATION = 'undergo operation'
    DISCHARGING = 'discharging'
    DISCHARGED = 'discharged'

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    def __str__(self):
        return self.value

class TreatmentTypeChoice(str, Enum):
    THEORY = 'theory'
    SURGERY = 'surgery'

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    def __str__(self):
        return self.value

class StaffTypeChoice(str, Enum):
    OPERATION = 'operation'
    ADMINISTRATION = 'administration'

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    def __str__(self):
        return self.value

class EmployeeTypeChoice(str, Enum):
    RECETIONIST = 'receptionist'
    ADMINISTRATOR = 'administrator'

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    def __str__(self):
        return self.value

class Hospital(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    address = models.CharField(max_length=256, null=False, blank=False)
    phone_number = PhoneField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Department(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    hospital = models.ForeignKey(Hospital, null=False, blank=False,
        on_delete=models.CASCADE, related_name="hospital")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Staff(models.Model):
    type = models.CharField(max_length=32, choices=StaffTypeChoice.choices(),
        default=StaffTypeChoice.OPERATION)
    name = models.CharField(max_length=256, null=False, blank=False)
    speciality = models.CharField(max_length=256, null=False, blank=False)
    department = models.ForeignKey(Department, null=False, blank=False,
        on_delete=models.CASCADE, related_name="department")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    gender = models.CharField(max_length=32, choices=GenderChoice.choices(),
        default=GenderChoice.MALE)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=256, null=False, blank=False)
    phone_number = PhoneField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Doctor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="doctor_person")
    speciality = models.CharField(max_length=256, null=False, blank=False)
    is_surgeon = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, null=False, blank=False,
        on_delete=models.CASCADE, related_name="doctor_staff")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Nurse(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="nurse_person")
    degree = models.CharField(max_length=256, null=False, blank=False)
    staff = models.ForeignKey(Staff, null=False, blank=False,
        on_delete=models.CASCADE, related_name="nurse_staff")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="patient_person")
    accepted_date = models.DateField()
    sickness_history = models.CharField(max_length=1024, null=True, blank=True)
    allergies = models.CharField(max_length=1024, null=True, blank=True)
    status = models.CharField(max_length=32, choices=PatientStatusChoice.choices(),
        default=PatientStatusChoice.REGISTERED)
    doctor = models.ForeignKey(Doctor, null=False, blank=False,
        on_delete=models.CASCADE, related_name="responsible_doctor")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Diagnosis(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.CharField(max_length=1024, null=False, blank=False)
    specialist = models.ForeignKey(Doctor, null=False, blank=False,
        on_delete=models.CASCADE, related_name="specialist")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Examination(models.Model):
    type = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    cost = models.FloatField(null=False)
    patient = models.ForeignKey(Patient, null=False, blank=False,
        on_delete=models.CASCADE, related_name="tested_patient")
    diagnosis = models.OneToOneField(Diagnosis, on_delete=models.CASCADE, related_name="test_diagnosis")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Prescription(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.CharField(max_length=1024, null=False, blank=False)
    patient = models.ForeignKey(Patient, null=False, blank=False,
        on_delete=models.CASCADE, related_name="owner")
    diagnosis = models.OneToOneField(Diagnosis, on_delete=models.CASCADE, related_name="prescription_diagnosis")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Treatment(models.Model):
    type = models.CharField(max_length=32, choices=TreatmentTypeChoice.choices(),
        default=TreatmentTypeChoice.THEORY)
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.CharField(max_length=1024)
    cost = models.FloatField(null=False)
    patient = models.ForeignKey(Patient, null=False, blank=False,
        on_delete=models.CASCADE, related_name="patient")
    diagnosis = models.ForeignKey(Diagnosis, null=False, blank=False,
        on_delete=models.CASCADE, related_name="diagnosis")
    staff = models.ForeignKey(Staff, null=False, blank=False,
        on_delete=models.CASCADE, related_name="treatment_staff")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

class Employee(models.Model):
    type = models.CharField(max_length=32, choices=EmployeeTypeChoice.choices(),
        default=EmployeeTypeChoice.RECETIONIST)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="employee_person")
    staff = models.ForeignKey(Staff, null=False, blank=False,
        on_delete=models.CASCADE, related_name="employee_staff")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()