import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_asgi_application()

from django.test import TestCase
from  import TipoDocumento
# Create your tests here.

