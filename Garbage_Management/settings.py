"""
Django settings for Garbage_Management project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1kxfz+p4cx+zpti)*jg-(g@x^x0ij&gk3ol6$)%2t&m!m(#+h('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    # 'adminlte3',
    # 'adminlte3_theme',
    'django.contrib.auth',
    'jazzmin',
    'Home',
    'accounts',
    'django.contrib.admin',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'location_field.apps.DefaultConfig',
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

ROOT_URLCONF = 'Garbage_Management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR),'Templates'],

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

WSGI_APPLICATION = 'Garbage_Management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'Garbage2',
        'USER':'postgres',
        'PASSWORD':'root',
        'HOST':'localhost'
    }
}

AUTH_USER_MODEL = 'accounts.Account'
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'accounts.Account'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_DIR=os.path.join(BASE_DIR,'static')
STATIC_URL = 'static/'
STATICFILES_DIRS=[
        STATIC_DIR
]
# STATIC_ROOT=os.path.join(BASE_DIR,'assets')


MEDIA_URL='/images/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')
# #SMTP Configruation
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'dreamlandpark2705@gmail.com'
# EMAIL_HOST_PASSWORD = 'cexqzmfkphlyefab'
# ACCOUNT_EMAIL_VERIFICATION = 'none'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'garbagemanagement3@gmail.com'
DEFAULT_FROM_EMAIL = 'garbagemanagement3@gmail.com'
SERVER_EMAIL = 'garbagemanagement3@gmail.com'
EMAIL_HOST_PASSWORD = 'rpsshxhehqzgryul'
RECAPTCHA_PUBLIC_KEY = '6Lc2Rr0kAAAAAODy6HzDXmW6oyRcI3DgoSRk8UuQ'
RECAPTCHA_PRIVATE_KEY = '6Lc2Rr0kAAAAAJJanfb28XfvhAqQjCO0McMcbRH4'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
RAZORPAY_API_KEY="rzp_test_n7irR21xKIBPBj"
RAZORPAY_API_SECRET_KEY="4DNQcF66EGnIWV2huNtZXz0Q"
EMAIL_USE_TLS = True



LOCATION_FIELD = {
    'search.provider': 'google',

}


LOCATION_FIELD = {
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': '',
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'GOOGLE',
}