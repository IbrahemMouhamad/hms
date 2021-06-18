# Copyright (C) 2021 Ibrahem Mouhamad

import os
import sys

from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = str(Path(__file__).parents[2])

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
INTERNAL_IPS = ['127.0.0.1']


try:
    sys.path.append(BASE_DIR)
    from keys.secret_key import SECRET_KEY # pylint: disable=unused-import
except ImportError:
    from django.utils.crypto import get_random_string
    keys_dir = os.path.join(BASE_DIR, 'keys')
    if not os.path.isdir(keys_dir):
        os.mkdir(keys_dir)
    with open(os.path.join(keys_dir, 'secret_key.py'), 'w') as f:
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        f.write("SECRET_KEY = '{}'\n".format(get_random_string(50, chars)))
    from keys.secret_key import SECRET_KEY


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hms.apps.authentication',
    'hms.apps.engine',
    'sendfile',
    'dj_pagination',
    'rules',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'drf_yasg',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'corsheaders',
    'rest_auth.registration',
    'phone_field'
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'hms.apps.authentication.auth.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_VERSIONING_CLASS':
        # Don't try to use URLPathVersioning. It will give you /api/{version}
        # in path and '/api/docs' will not collapse similar items (flat list
        # of all possible methods isn't readable).
        'rest_framework.versioning.NamespaceVersioning',
    # Need to add 'api-docs' here as a workaround for include_docs_urls.
    'ALLOWED_VERSIONS': ('v1', 'api-docs'),
    'DEFAULT_PAGINATION_CLASS':
        'hms.apps.engine.pagination.CustomPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'),

    # Disable default handling of the 'format' query parameter by REST framework
    'URL_FORMAT_OVERRIDE': 'scheme',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/minute',
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # FIXME
    # 'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dj_pagination.middleware.PaginationMiddleware',
]

UI_URL = ''

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

ROOT_URLCONF = 'hms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hms.wsgi.application'

# Django Auth
DJANGO_AUTH_TYPE = 'BASIC'
DJANGO_AUTH_DEFAULT_GROUPS = []
LOGIN_URL = 'rest_login'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# https://github.com/pennersr/django-allauth
ACCOUNT_EMAIL_VERIFICATION = 'none'
# set UI url to redirect after a successful e-mail confirmation
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/auth/login'
OLD_PASSWORD_FIELD_ENABLED = True

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.getenv('TZ', 'Etc/UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

CSRF_COOKIE_NAME = "csrftoken"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
os.makedirs(STATIC_ROOT, exist_ok=True)

DATA_ROOT = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_ROOT, exist_ok=True)

MEDIA_DATA_ROOT = os.path.join(DATA_ROOT, 'data')
os.makedirs(MEDIA_DATA_ROOT, exist_ok=True)

LOGS_ROOT = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOGS_ROOT, exist_ok=True)

MIGRATIONS_LOGS_ROOT = os.path.join(LOGS_ROOT, 'migrations')
os.makedirs(MIGRATIONS_LOGS_ROOT, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': [],
            'formatter': 'standard',
        },
        'server_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'filename': os.path.join(BASE_DIR, 'logs', 'hms_server.log'),
            'formatter': 'standard',
            'maxBytes': 1024*1024*50, # 50 MB
            'backupCount': 5,
        },
    },
    'loggers': {
        'hms.server': {
            'handlers': ['console', 'server_file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },

        'hms.client': {
            'handlers': [],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },

        'django': {
            'handlers': ['console', 'server_file'],
            'level': 'INFO',
            'propagate': True
        }
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'