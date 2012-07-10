import os.path

# Library Settings

DASORNIS_WORKING_DIR = os.path.abspath(__file__).replace('config/__init__.py','')

# Project Settings
DEBUG = True
WORKING_DIR = os.path.dirname(__file__)
DB_DRIVER = None
DB_USER = 'dasornis'
DB_PASSWORD = "dasornis"
DB_NAME = "dasornis"
DB_HOST = "localhost"
LOG_FILE = 'dasornislog'
TEMPLATE_ENGINE = ''
TEMPLATE_DIRS = (
# Template directories comes here
)

ENABLE_I18N = True
I18N_PACKAGE = None
DEFAULT_LANG = None

'''
Importing project configuration file if exists
'''
import os
config_module = os.environ.get('DASORNIS_CONFIG_MODULE') or 'dasornisconf'

try:
  exec "from %s import *"%config_module
except ImportError:
  from dasornis.log import logging
  logging.warning("Could not import configuration module '%s'."%config_module)
