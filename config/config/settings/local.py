from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', 
default='&k67oac45)rq%24h51tdu0c=#5#oq4e(d-+oyajrka!1e!v)rz')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
