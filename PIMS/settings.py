"""
Django settings for PIMS project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

from cassandra import ConsistencyLevel
from corsheaders.defaults import default_methods,default_headers
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
#STATIC_DIR = os.path.join(BASE_DIR,'static')
#MEDIA_DIR = os.path.join(BASE_DIR,'media')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z2mps+d5@mmws!$i3@g5_g4w=$%!1g-6#!ch)(bmzs%s1=(wgl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'Users.User'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'searchengine',
    'corsheaders',
    'userprofile',
    'link',
    'organiser',
    'Users',
    'collection',
    'connections',
    'sharedwithme',
    'trends'
]
INSTALLED_APPS = ['django_cassandra_engine'] + INSTALLED_APPS
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

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = list(default_methods)
mycustomheader = 'Access-Control-Allow-Origin'
CORS_ALLOW_HEADERS = list(default_headers)+[mycustomheader]
CORS_PREFLIGHT_MAX_AGE = 86400
# CSRF_TRUSTED_ORIGINS = [
#     'http://localhost:4200/'
# ]
ROOT_URLCONF = 'PIMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[os.path.join(BASE_DIR, 'templates')],
            #[TEMPLATE_DIR,],
            #[BASE_DIR / 'templates'],
            #[os.path.join(BASE_DIR, 'templates')],

        #  [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'PIMS.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
'cassandra': {
            'ENGINE': 'django_cassandra_engine',
            'NAME': 'db',
            'USER': 'user',
            'PASSWORD': 'pass',
            'TEST_NAME': 'test_db',
            'HOST': '127.0.0.1',
            'OPTIONS': {
                'replication': {
                    'strategy_class': 'SimpleStrategy',
                    'replication_factor': 1
                },
                'connection': {
                    'consistency': ConsistencyLevel.LOCAL_ONE,
                    'retry_connect': True
                    # + All connection options for cassandra.cluster.Cluster()
                },
                'session': {
                    'default_timeout': 10,
                    'default_fetch_size': 10000
                    # + All options for cassandra.cluster.Session()
                }
            }
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = 'home'

#STATICFILES_DIRS = [STATIC_DIR,]
#MEDIA_ROOT = MEDIA_DIR
#MEDIA_URL = ‘/media/’
#LOGIN_URL = ‘/dappx/user_login/’