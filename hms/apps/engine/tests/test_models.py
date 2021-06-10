# Copyright (C) 2021 Ibrahem Mouhamad

from django.test import TestCase
from hms.apps.engine.models import Hospital

class HosptialTestCase(TestCase):
    def setUp(self):
        Hospital.objects.create(name="Hospital1", address="Hospital1 address")
        Hospital.objects.create(name="Hospital2", address="Hospital2 address")

    def test_hospital(self):
        hosptial1 = Hospital.objects.get(name="Hospital1")
        hosptial2 = Hospital.objects.get(name="Hospital2")
        self.assertEqual(hosptial1.address, "Hospital1 address")
        self.assertEqual(hosptial2.address, "Hospital2 address")