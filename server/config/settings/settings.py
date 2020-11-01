import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = '!6xmo&@!7dzw8p6yxjnj&&1lur%4+fs!r2tuzb#6j(64s@m6)*'
ROOT_URLCONF = 'config.urls'
ALLOWED_HOSTS = ['*']
SITE_ID = 1

##################################################################
# Debug settings (with docker)
##################################################################

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

##################################################################
# Templates, middleware settings
##################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

##################################################################
# Static files settings (CSS, JavaScript, Images)
##################################################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = ('static',)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

FILE_UPLOAD_PERMISSIONS = 0o777
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o777

##################################################################
# Debug toolbar settings
##################################################################

if DEBUG:
    from .installed_apps import *


    def show_toolbar(request):
        from django.conf import settings
        return settings.DEBUG


    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    }
    MIDDLEWARE = [
                     'debug_toolbar.middleware.DebugToolbarMiddleware', ] + MIDDLEWARE
    INSTALLED_APPS += ['debug_toolbar', ]

##################################################################
# Celery settings
##################################################################

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", 'redis://redis:6379/0')
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_BEAT_SCHEDULE = {
    "get_random_fact": {"task": "apps.meow.tasks.get_random_fact",
                        "schedule": 5.0}
}

##################################################################
# Channels settings
##################################################################

ASGI_APPLICATION = "config.routing.application"
WSGI_APPLICATION = "config.wsgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(os.environ.get("REDIS_CHANNEL_LAYER_HOST",
                                      'redis://redis:6379/1'))],
        },
    },
}
