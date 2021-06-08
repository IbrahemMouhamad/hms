# Copyright (C) 2021 Ibrahem Mouhamad

from django.apps import AppConfig


class EngineConfig(AppConfig):
    name = 'hms.apps.engine'

    '''
    def ready(self):
        # Required to define signals in application
        import cvat.apps.engine.signals
        # Required in order to silent "unused-import" in pyflake
        assert cvat.apps.engine.signals
    '''
