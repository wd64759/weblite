import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'admin'
SECRET_CODE= 'admin'
DB_URI = 'sqlite:////{}'.format(os.path.join(_basedir, 'weblite.db'))
DB_CONN_OPTIONS = {}

# remove the reference of OS. is it necessary ?
del os
