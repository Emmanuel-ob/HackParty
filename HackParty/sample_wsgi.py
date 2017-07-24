import os
import sys

path = '/home/techmind/HackParty'
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'HackParty.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HackParty.settings")

application = StaticFilesHandler(get_wsgi_application())