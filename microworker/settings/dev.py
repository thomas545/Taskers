from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS += ['debug_toolbar',]


MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]


# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': '',
# }

DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': True,
    # Panel options
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds
}

INTERNAL_IPS = [
    '127.0.0.1',
]