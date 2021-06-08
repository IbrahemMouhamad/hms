# Copyright (C) 2021 Ibrahem Mouhamad

from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    name = 'hms.apps.authentication'

    def ready(self):
        from .auth import register_signals

        register_signals()