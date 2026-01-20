from decouple import config
from .base import *

  
DJANGO_ENV = config('DJANGO_ENV')


if DJANGO_ENV == 'development':
    from .development import *
elif DJANGO_ENV == 'production':
    from .production import *
else:
    raise Exception('DJANGO_ENV no installed.')