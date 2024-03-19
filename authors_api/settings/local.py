from .base import *
from .base import env


DEBUG=True

SECRET_KEY =env("DJANGO_SECRET_KEY",default='django-insecure-tfu)o3zuc!=2l&&)70(*3f15b^%63-%pkxf^39ij$hu^)sqc)@')
ALLOWED_HOSTS = ["localhost","0.0.0.0","127.0.0.1"]
