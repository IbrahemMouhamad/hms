# Copyright (C) 2021 Ibrahem Mouhamad

from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('person', 'speciality', 'is_surgeon', 'staff', 'created_date', 'updated_date')


