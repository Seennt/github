"""
!!! This file is excluded for production. Therefor it is added to .gitignore.

Django settings for system project on local development server. For more info, see:
https://coderwall.com/p/q5nepa/how-to-setup-local_settings-py-for-your-django-1-4-2-project

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^!29f51-fid11(yfi2@%q(y5&=u6jb!&8vz=b*wa#-e)4=y1#n"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'local-postgresql-51412',
        'USER': 'postgres',
        'PASSWORD': 'u0360i3',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Allow all host headers
ALLOWED_HOSTS = ['localhost']
