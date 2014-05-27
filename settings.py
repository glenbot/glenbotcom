DEBUG = True

APP_NAME = 'Glenbot'
APP_TAGLINE = 'Open source code and articles by Glenbot'

CODRSPACE_API_URL = 'http://codrspace.com/api/v1'
CODRSPACE_API_USERNAME = None
CODRSPACE_API_KEY = None

try:
    from local_settings import *
except ImportError:
    pass
