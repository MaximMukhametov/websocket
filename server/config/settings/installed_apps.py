INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "channels",
]

LOCAL_APPS = [
    'apps.table',
]

INSTALLED_APPS += LOCAL_APPS

LOCAL_MIGRATIONS = [app_path.split('.')[1] for app_path in LOCAL_APPS]

MIGRATION_PATH = 'config.migrations.'

MIGRATION_MODULES = {app_name: MIGRATION_PATH + app_name for app_name in LOCAL_MIGRATIONS}
