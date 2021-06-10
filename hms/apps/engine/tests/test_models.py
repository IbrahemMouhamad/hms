# Copyright (C) 2021 Ibrahem Mouhamad

from django.test import TestCase
from hms.apps.engine.models import Hospital, Department, Staff, StaffTypeChoice

class HospitalTestCase(TestCase):
    def setUp(self):
        Hospital.objects.create(name="Hospital1", address="Hospital1 address")
        Hospital.objects.create(name="Hospital2", address="Hospital2 address")

    def test_hospital(self):
        hospital1 = Hospital.objects.get(name="Hospital1")
        hospital2 = Hospital.objects.get(name="Hospital2")
        self.assertEqual(hospital1.address, "Hospital1 address")
        self.assertEqual(hospital2.address, "Hospital2 address")

class DepartmentTestCase(TestCase):
    def setUp(self):
        hospital1 = Hospital.objects.create(name="hospital1", address="Hospital1 address")
        Department.objects.create(name="department1", hospital = hospital1)
        Department.objects.create(name="department2", hospital = hospital1)

    def test_department(self):
        department1 = Department.objects.get(name="department1")
        department2 = Department.objects.get(name="department2")
        self.assertEqual(department1.hospital.address, "Hospital1 address")
        self.assertEqual(department2.name, "department2")

class StaffTestCase(TestCase):
    def setUp(self):
        hospital1 = Hospital.objects.create(name="hospital1", address="Hospital1 address")
        department1 = Department.objects.create(name="department1", hospital = hospital1)
        Staff.objects.create(name="staff1", speciality="staff1 speciality", department = department1)

    def test_department(self):
        staff1 = Staff.objects.get(name="staff1")
        self.assertEqual(staff1.department.name, "department1")
        self.assertEqual(staff1.type, StaffTypeChoice.OPERATION)