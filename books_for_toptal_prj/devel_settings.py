DEBUG = True

TIME_ZONE = 'Europe/Kiev'

ADMINS = (
    ('Sergey Dymchenko', 'kit1980@gmail.com'),
    )
MANAGERS = ADMINS

MEDIA_URL = 'http://127.0.0.1/media.books/'
ADMIN_MEDIA_PREFIX = 'http://127.0.0.1/admin-media.books/'

#CACHE_BACKEND = "dummy:///"

#CACHE_MIDDLEWARE_SECONDS = 1
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#CACHE_MIDDLEWARE_KEY_PREFIX = 'books_progopedia_com'

## MIDDLEWARE_CLASSES += (
##     'debug_toolbar.middleware.DebugToolbarMiddleware',
## )
## INSTALLED_APPS += ('debug_toolbar', )
## INTERNAL_IPS = ('127.0.0.1')
