import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'admin'
SECRET_CODE= 'admin'
DATABASE_URI = os.path.join(_basedir, 'weblite.db')
DATABASE_CONNECT_OPTIONS = {}

# remove the reference of OS. is it necessary ?
del os
