from email.policy import default
from pathlib import Path
import os
import dj_database_url
import django_heroku
from dotenv import find_dotenv, load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'izuminapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'izuminapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'izuminapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

load_dotenv(find_dotenv())
# {'NAME': 'pj_db', 'USER': 'root', 'PASSWORD': 'Class9Team5', 'HOST': 'localhost', 'PORT': '', 'CONN_MAX_AGE': 600, 'ENGINE': 'django.db.backends.mysql'}
default = dj_database_url.config(conn_max_age=600)
# default['OPTIONS'] = {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", 'charset': 'utf8mb4'} #MySQL用
# postgresだとmigrate実行前に $ pg_ctl start -D "C:/Program Files/PostgreSQL/14/data"
DATABASES = {
    'default': default,
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


DEFAULT_AUTO_FIELD='django.db.models.AutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'IOfiles/image/')
STATIC_URL = 'IOfiles/image/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


if DEBUG :
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    SECRET_KEY = SECRET_KEY
else :
    django_heroku.settings(locals())
    SECRET_KEY = 'q93+xpfmw33@ug#5xea$z6i1p!yhn(qxi4-88=-npj^ppftd+a'