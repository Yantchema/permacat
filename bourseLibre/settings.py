# -*- coding: utf-8 -*-
"""
Django settings for bourseLibre project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

 python manage.py createsuperuser
python manage.py migrate --run-syncdb

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
try:
    import dj_database_url
except:
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    SECRET_KEY = 'aersdfgsfdgsdthhfhdjd'
else:
    SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['127.0.0.1', 'demo-permacat.herokuapp.com']

# Application definition

# pip install django-fontawesome django-model_utils django-debug_toolbar django-haystack django-bootstrap django-extensions django-leaflet django-filter django-rest-framework django-scheduler django-widget-tweaks

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.sites',
    #'django.contrib.gis',
    'bootstrap','fontawesome','cookielaw',
    'haystack',
    #'debug_toolbar',
    'model_utils',
    #'address',
    'bourseLibre',
    'blog',
    'django_extensions',
    'django_filters',
    'rest_framework',
    'schedule','djangobower',
    'widget_tweaks',
    'leaflet'
    #"geoposition",
    #"geodjango",
    #'osm_field',
    #'location_field.apps.DefaultConfig',
    #'sitetree',
    #'panier',
    #'location-field',
    #'polymorphic',  # We need polymorphic installed for the shop
    #'shop',  # The django SHOP application
    #'shop.addressmodel',  # The default Address and country models
    # 'regist#ration'
)

# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.common.BrokenLinkEmailsMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.core.context_processors.request',
    'whitenoise.middleware.WhiteNoiseMiddleware',
   #'debug_toolbar.middleware.DebugToolbarMiddleware',
]


ROOT_URLCONF = 'bourseLibre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'string_if_invalid': 'Invalid: "%s"',
            'libraries': {'is_numeric': 'bourseLibre.templatetags.app_filters', }
        },
    },
]

WSGI_APPLICATION = 'bourseLibre.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
     'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.db'),
    }
}
#try:
#DATABASES = {}
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# except:


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    #{    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
#         'URL': 'http://127.0.0.1:8000/',
#         'INDEX_NAME': 'haystack',
#     },
# }y
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#    },
#}
HAYSTACK_CONNECTIONS = {
  'default': {
    'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
    'PATH': os.path.join(os.path.dirname(__file__), 'search_index'),
  },
}
AUTH_USER_MODEL = 'bourseLibre.Profil'
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

SITE_ID = 1

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = "l d F Y"
DATE_FORMAT_COURT = "d F Y"
DATE_FORMAT_COURT_HEURE = "d F Y, G:i"
#DATETIME_INPUT_FORMATS = '%d/%m/%Y'
#TIME_INPUT_FORMATS = '%H:%M'
SHORT_DATE_FORMAT = "d F Y"
#DATE_INPUT_FORMATS = ('%d/%m/%Y',)


LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

INTERNAL_IPS = ['127.0.0.1']

########################

# Email settings
SERVER_EMAIL = 'permacat66@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'lml666'
EMAIL_HOST_USER = SERVER_EMAIL
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# MANAGERS: It specifies a list of people to send broken link emails for 404 NOT FOUND errors. It's accepts emails in the same format as ADMINS.
MANAGERS = [
    ('eloi', 'permacat66@email.com'),
]
ADMINS = [
    ('eloi', 'permacat66@gmail.com'),
]


########################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL= 'images/'
MEDIA_ROOT= BASE_DIR + "../staticstorage/images/"


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# LOCATION_FIELD = {
#     'map.provider': 'openstreetmap',
# }

#GEOPOSITION_GOOGLE_MAPS_API_KEY = ' AIzaSyCmGcPj0ti_7aEagETrbJyHPbE3U6gVfSA '

#GOOGLE_API_KEY = 'AIzaSyCmGcPj0ti_7aEagETrbJyHPbE3U6gVfSA'

#GOOGLE_API_KEY = 'AIzaSyC10StWuCZHLPmSZCyfNEdmgZ7CTqdngy0'

LEAFLET_CONFIG = {
'DEFAULT_CENTER': (42.7201813, 2.8876436),
'DEFAULT_ZOOM': 10,
'MIN_ZOOM': 3,
'MAX_ZOOM': 18,
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'cache_bourseLibre'
#     }
# }


#STATICFILES_FINDERS= ['djangobower.finders.BowerFinder',]
#BOWER_COMPONENTS_ROOT = BASE_DIR +'/components/'
#BOWER_INSTALLED_APPS = (
#    'jquery',
#    'jquery-ui',
#    'bootstrap'
#)

PHONENUMBER_DEFAULT_REGION = 'INTERNATIONAL'
