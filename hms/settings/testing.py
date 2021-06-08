# Copyright (C) 2021 Ibrahem Mouhamad

from .development import *
import tempfile

_temp_dir = tempfile.TemporaryDirectory(suffix="hms")

DATA_ROOT = os.path.join(_temp_dir.name, 'data')
os.makedirs(DATA_ROOT, exist_ok=True)

MEDIA_DATA_ROOT = os.path.join(DATA_ROOT, 'data')
os.makedirs(MEDIA_DATA_ROOT, exist_ok=True)

# To avoid ERROR django.security.SuspiciousFileOperation:
# The joined path (...) is located outside of the base path component
MEDIA_ROOT = _temp_dir.name

# Suppress all logs by default
for logger in LOGGING["loggers"].values():
    if isinstance(logger, dict) and "level" in logger:
        logger["level"] = "ERROR"

LOGGING["handlers"]["server_file"] = LOGGING["handlers"]["console"]

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

# When you run ./manage.py test, Django looks at the TEST_RUNNER setting to
# determine what to do. By default, TEST_RUNNER points to
# 'django.test.runner.DiscoverRunner'. This class defines the default Django
# testing behavior.