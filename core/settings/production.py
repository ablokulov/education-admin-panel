from decouple import config,Csv
from .base import BASE_DIR

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',default=False,cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS',cast=Csv())


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),      # Name of the database you created
        'USER': config('DB_USER'),      # Database username
        'PASSWORD': config('DB_PASS'),  # User password
        'HOST': config('DB_HOST'),      # Or the IP/hostname of your DB server
        'PORT': config('DB_PORT'),      # Default PostgreSQL port
    }
}


STATIC_ROOT = BASE_DIR / "staticfiles"