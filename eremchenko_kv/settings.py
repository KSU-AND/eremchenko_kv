"""
Django settings for eremchenko_kv project.
"""
import os
from pathlib import Path
from dotenv import dotenv_values


secrets = dotenv_values()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = secrets.get('SECRET_KEY')
TLG_TOKEN = secrets.get("TLG_TOKEN")
TLG_ADMIN_ID = secrets.get("TLG_ADMIN_ID")

DEBUG = secrets.get('DEBUG') == 'True'

if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1']
    TLG_ADMIN_ID = secrets.get("TLG_TESTER_ID")
else:
    ALLOWED_HOSTS = [secrets.get('MAIN_HOST')]


# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'fut_in_pst_typology'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eremchenko_kv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'eremchenko_kv/templates',
            'fut_in_pst_typology/templates',
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

WSGI_APPLICATION = 'eremchenko_kv.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': secrets.get('DB_NAME'),
        'USER': secrets.get('DB_USER'),
        'PASSWORD': secrets.get('DB_PASSWORD'),
        'HOST': secrets.get('DB_HOST'),
        'PORT': secrets.get('DB_PORT'),
    }
}


# Password validation
AUTH_USER_MODEL = 'accounts.User'
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
