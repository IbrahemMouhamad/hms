# Copyright (C) 2021 Ibrahem Mouhamad

from unittest.mock import patch

from django.test import TestCase
from django.db.models import QuerySet
from django.contrib.auth.models import Group, User

from hms.apps.engine.models import (
    Hospital, Department, Staff, Person, Doctor, StaffTypeChoice, Patient, Prescription,
    Diagnosis
)


def create_dummy_db_hospital(obj, name, address):
    hospital = Hospital.objects.create(name=name, address=address)
    return hospital

def create_dummy_db_department(obj, name, hospital):
    department = Department.objects.create(
        name=name,
        hospital=create_dummy_db_hospital(obj, hospital, "hospital1 address")
    )
    return department

def create_dummy_db_staff(obj, name, department):
    staff = Staff.objects.create(
        name=name,
        speciality="staff speciality",
        department=create_dummy_db_department(obj, department, "hospital1")
    )
    return staff

def create_dummy_db_users(cls):
    (group_admin, _) = Group.objects.get_or_create(name="admin")
    (group_user, _) = Group.objects.get_or_create(name="user")
    (group_receptionist, _) = Group.objects.get_or_create(name="receptionist")
    (group_doctor, _) = Group.objects.get_or_create(name="doctor")
    (group_nurse, _) = Group.objects.get_or_create(name="nurse")

    user_admin = User.objects.create_superuser(username="admin", email="",
        password="admin")
    user_admin.groups.add(group_admin)
    user_normal_user = User.objects.create_user(username="nuser", password="nuser")
    user_normal_user.groups.add(group_user)
    user_receptionist = User.objects.create_user(username="receptionist", password="receptionist")
    user_receptionist.groups.add(group_receptionist)
    user_doctor = User.objects.create_user(username="doctor", password="doctor")
    user_doctor.groups.add(group_doctor)
    user_nurse = User.objects.create_user(username="nurse", password="nurse")
    user_nurse.groups.add(group_nurse)
    user_dummy = User.objects.create_user(username="duser", password="duser")
    user_dummy.groups.add(group_user)

    cls.admin = user_admin
    cls.normal_user = user_normal_user
    cls.receptionist = user_receptionist
    cls.doctor = user_doctor
    cls.nurse = user_nurse
    cls.dummy_user = user_dummy

def create_dummy_db_user(cls, username):
    user = User.objects.create_user(username=username, email="",
        password=username)
    return user

def create_dummy_db_person(cls, user):
    person = Person.objects.create(
        user=user,
        birth_date = "1977-01-01",
        address = "fake address"
    )
    return person

def create_dummy_db_doctor(cls, name):
    doctor = Doctor.objects.create(
        person=create_dummy_db_person(cls, create_dummy_db_user(cls, name)),
        staff = create_dummy_db_staff(cls, "staff1", "department1"),
        speciality = "fake speciality"
    )
    return doctor

def create_dummy_db_patient(cls, name, doctor):
    patient = Patient.objects.create(
        person=create_dummy_db_person(cls, create_dummy_db_user(cls, name)),
        doctor = doctor,
        accepted_date = "2021-06-11"
    )
    return patient

class HospitalTestCase(TestCase):
    def setUp(self):
        self.name = "hospital1"
        self.address = "hospital1 address"

    @classmethod
    def setUpTestData(cls):
        cls.hospital = create_dummy_db_hospital(cls, "hospital1", "hospital1 address")

    def test_hospital_creation_successed(self):
        hospital1 = Hospital.objects.get(name=self.name)
        self.assertEqual(hospital1.address, self.address)

    def test_hospital_get_failed(self):
        self.assertRaises(Hospital.DoesNotExist, Hospital.objects.get, name="wrong name")

class DepartmentTestCase(TestCase):
    def setUp(self):
        self.name = "department1"
        self.hospital_name = "hospital1"

    @classmethod
    def setUpTestData(cls):
        cls.department = create_dummy_db_department(cls, "department1", "hospital1")

    def test_department_creation_successed(self):
        department1 = Department.objects.get(name=self.name)
        hospital = Hospital.objects.get(name=self.hospital_name)
        self.assertEqual(department1.hospital.name, hospital.name)

    def test_department_get_failed(self):
        self.assertRaises(Department.DoesNotExist, Department.objects.get, name="wrong name")

class StaffTestCase(TestCase):
    def setUp(self):
        self.name = "staff1"
        self.department_name = "department1"
        self.hospital_name = "hospital1"

    @classmethod
    def setUpTestData(cls):
        cls.hospital = create_dummy_db_hospital(cls, "hospital1", "hospital1 address")
        cls.department = create_dummy_db_department(cls, "department1", cls.hospital)
        cls.staff = create_dummy_db_staff(cls, "staff1", department = "department1")

    def test_staff_creation_successed(self):
        staff = Staff.objects.get(name=self.name)
        self.assertEqual(staff.type, StaffTypeChoice.OPERATION)
        self.assertEqual(staff.department.name, self.department_name)
        self.assertEqual(staff.department.hospital.name, self.hospital_name)

    def test_staff_get_failed(self):
        self.assertRaises(Staff.DoesNotExist, Staff.objects.get, name="wrong name")


class DoctorTestCase(TestCase):
    def setUp(self):
        self.name = "doctor1"
        self.staff_name = "staff1"
        self.patient1_name = "patient1"
        self.patient1_name = "patient1"
        self.diagnosis1_name = "diagnosis1 name"
        self.diagnosis1_des = "diagnosis1 description"
        self.prescription1_name = "prescription1 name"
        self.prescription1_des = "prescription1 description"

    @classmethod
    def setUpTestData(cls):
        cls.doctor = create_dummy_db_doctor(cls, "doctor1")
        cls.patient1 = create_dummy_db_patient(cls, "patient1", cls.doctor)
        cls.patient2 = create_dummy_db_patient(cls, "patient2", cls.doctor)
        cls.patient3 = create_dummy_db_patient(cls, "patient3", cls.doctor)

    def test_doctor_creation_successed(self):
        doctor = Doctor.objects.get(person__user__username=self.name)
        self.assertEqual(doctor.is_surgeon, False)
        self.assertEqual(doctor.staff.name, self.staff_name)

    def test_doctor_get_failed(self):
        self.assertRaises(Doctor.DoesNotExist, Doctor.objects.get, person__user__username="wrong name")

    def test_get_patients_successed(self):
        doctor1 = Doctor.objects.get(person__user__username=self.name)
        patients = doctor1.get_patients()
        self.assertIsInstance(patients, QuerySet)

    def test_write_prescription_successed(self):
        doctor1 = Doctor.objects.get(person__user__username=self.name)
        patient1 = Patient.objects.get(person__user__username=self.patient1_name)
        # checkup the paitent
        diagnosis1 = doctor1.check_up(name=self.diagnosis1_name, description=self.diagnosis1_des)
        # write a prescription for the patient
        doctor1.write_prescription(patient1, name=self.prescription1_name, description=self.prescription1_des, diagnosis=diagnosis1.name)
        # write_prescription it is a void message but it add a prescription for the patient
        # check if there is a single prescription for the patient
        prescriptions = Prescription.objects.all().filter(patient__id = patient1.id)
        self.assertIsInstance(prescriptions, QuerySet)
        self.assertEqual(prescriptions.count(), 1)

    def test_write_prescription_failed(self):
        doctor1 = Doctor.objects.get(person__user__username=self.name)
        patient1 = Patient.objects.get(person__user__username=self.patient1_name)
        # writing a prescription for the patient should failed because of wrong diagnosis object
        self.assertRaises(
            Diagnosis.DoesNotExist,
            doctor1.write_prescription,
                patient1,
                name=self.prescription1_name,
                description=self.prescription1_des,
                diagnosis="wrong name"
            )


def mock_get_dector():
    user = User(username="doctor1", email="",password="doctor1")
    person = Person(user=user,birth_date = "1977-01-01",address = "fake address")
    staff = Staff(name="staff1")
    return Doctor(person=person, staff=staff, speciality = "fake speciality")


class DoctorTestCaseUsingMock(TestCase):
    def setUp(self):
        self.name = "doctor1"
        self.staff_name = "staff1"

    @patch("hms.apps.engine.models.Doctor.objects.get", mock_get_dector)
    def test_doctor_creation_successed(self):
        doctor = Doctor.objects.get()
        self.assertEqual(doctor.is_surgeon, False)
        self.assertEqual(doctor.staff.name, self.staff_name)
