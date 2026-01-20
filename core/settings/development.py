from decouple import config,Csv
from .base import INSTALLED_APPS,MIDDLEWARE
from .base import BASE_DIR

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',default=False,cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS',cast=Csv())

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_DIRS = [
    BASE_DIR / "static"
]

INTERNAL_IPS = [
    "127.0.0.1",
]