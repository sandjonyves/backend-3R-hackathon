"""
Django settings for Backend project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
import environ
from os import getenv
from dotenv import load_dotenv
from urllib.parse import urlparse

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR/'.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a5!909yl3=n4ws5$6$e1%)z8%%_r8!ig!l6%v7-f-6*_)pucq='

# SECURITY WARNING: don't run with debug turned on in production!


load_dotenv(BASE_DIR / '.env')

# Remplacer la section DATABASES dans settings.py avec cette configuration
tmpPostgres = urlparse(env("DATABASE_URL"))

DEBUG = True

ALLOWED_HOSTS = [
    '*',
]
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
  'http://localhost:5174',
    # Autres domaines autorisés si nécessaire
]

# Application definition

INSTALLED_APPS = [
    # 'django'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


   'rest_framework_swagger',       
    'rest_framework',            
    'drf_yasg',
    'django_filters',
    'rest_framework_simplejwt',
    'corsheaders',

    'account',
   
    'app',
    # 'store',
]

MIDDLEWARE = [
         'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Backend.urls'

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

WSGI_APPLICATION = 'Backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# Add these at the top of your settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
          'NAME': tmpPostgres.path[1:],
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = '/media/'

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILS_DIRS =[BASE_DIR/'static/']


# STATICFILES_DIRS = [ 
#      os.path.join(BASE_DIR, 'static'), 
#  ] 
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        # ...
    ),

    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 10,

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
                                       
                                        #  'rest_framework.authentication.TokenAuthentication',
    
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]

    
    
}
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}
AUTH_USER_MODEL = 'account.CustomUser'



# DONNEES REQUIS POUR ENVOYER LE MAIL

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sandjonyves@gmail.com'
EMAIL_HOST_PASSWORD ='vetqafchhoodnzpl'
# EMAIL_HOST_PASSWORD = 'wsfy/05/2004'
EMAIL_USE_TLS = True