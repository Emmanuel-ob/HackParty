"""
WSGI config for HackParty project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

#application = DjangoWhiteNoise(HackParty1)
application = get_wsgi_application()
application = DjangoWhiteNoise(application)


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HackParty.settings")

# application = Cling(get_wsgi_application())
