from .base import *
from .base import env


DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-tfu)o3zuc!=2l&&)70(*3f15b^%63-%pkxf^39ij$hu^)sqc)@",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

DEBUG = True
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@apiimperfect.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Havens"
