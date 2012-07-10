"""
DASORNIS CONFIGURATION FILE
"""
import os.path
import psycopg2

DEBUG = True
WORKING_DIR = os.path.dirname(__file__)
DB_DRIVER = psycopg2
DB_USER = "postgres"
DB_PASSWORD = "12345"
DB_NAME = "pud_test"
DB_HOST = "localhost"
LOG_FILE = '.log'
ENABLE_I18N = True
TEMPLATE_ENGINE = 'pythonstring'
TEMPLATE_DIRS = ('templates/')

if __name__ == '__main__':

    import sys,os
    sys.path.append(os.path.dirname(__file__)+'../')

    from dasornis.core.wsgi import serve
    import urls
    serve('localhost',8080,urls.map)
