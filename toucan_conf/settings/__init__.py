"""
Django settings for issues project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from .webpack import configureWebpackLoader

# BASE_DIR is where manage.py resides
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE-ME-IN-SECRETS-PY-FILE'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DEFAULT_FROM_EMAIL = 'toucan@brickwall.at'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'bootstrap3',
    'widget_tweaks',
    'channels',
    'rest_framework',
    'rest_framework_gis',
    'drf_multiple_model',
    'imagekit',
    'django_filters',
    'webpack_loader',
    'raven.contrib.django.raven_compat',
    # custom applications
    'toucan.organisations',
    'toucan.issues',
    'toucan.user_profile',
    'toucan.invitations',
    'toucan.media',
    'toucan.help',
    'toucan.branding',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

ROOT_URLCONF = 'toucan_conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'toucan/templates'),
            os.path.join(BASE_DIR, 'toucan/templates', 'allauth'),
        ],
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

WSGI_APPLICATION = 'toucan_conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'toucan',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')

WEBPACK_BUILD_DIR = os.path.join(BASE_DIR, 'frontend/production/')
WEBPACK_LOADER = configureWebpackLoader(WEBPACK_BUILD_DIR)

WEBPACK_ASSETS_DIR = os.path.join(BASE_DIR, 'frontend/assets/')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    ('frontend', WEBPACK_ASSETS_DIR),
    ('wp', WEBPACK_BUILD_DIR),  # this needs to be last, see dev config
]

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'toucan/fixtures/')
]

LOGIN_REDIRECT_URL = 'home'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "ROUTING": "toucan_conf.routing.channel_routing"
    },
}

# configure invitation system
INVITATION_REQUIRED = True
INVITATION_VALID_DAYS = 30

from .allauth import *

try:
    from .secrets import *
except ImportError:
    import warnings
    warnings.warn('No secrets file found in settings folder. Default settings assumed -- some things might be broken.')






