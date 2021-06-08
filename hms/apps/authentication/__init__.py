# Copyright (C) 2021 Ibrahem Mouhamad

default_app_config = 'hms.apps.authentication.apps.AuthenticationConfig'

from enum import Enum

class AUTH_ROLE(Enum):
    ADMIN = 'admin'
    RECETIONIST = 'receptionist'
    DOCTOR = 'doctor'
    NURSE = 'nurse'
    USER = 'user'

    def __str__(self):
        return self.value