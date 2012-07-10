"""
dasornis CONFIGURATION FILE
"""
import os.path
import psycopg2

WORKING_DIR = os.path.dirname(__file__)
DB_DRIVER = psycopg2
DB_USER = "azer"
DB_PASSWORD = "azer"
DB_NAME = "dasornis_test"
DB_HOST = "localhost"
LOG_FILE = '.log'
ENABLE_I18N = True
TEMPLATE_ENGINE = 'genshi'
TEMPLATE_DIRS = (
    'templates',
)
