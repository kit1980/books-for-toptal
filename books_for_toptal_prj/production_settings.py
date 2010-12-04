DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Sergey Dymchenko', 'kit1980@gmail.com'),
    )
MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'books_progopedia_com'       
DATABASE_USER = 'books'       
DATABASE_PASSWORD = 'my_password'

SITE_ID = 1

TIME_ZONE = 'Europe/Kiev'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/www/html/books.progopedia.com/static/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = 'http://books.progopedia.com/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7dddddujsfffffo9-8Dty(sdsi9jjwe8u8y78hiqwd9k'

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

#CACHE_MIDDLEWARE_SECONDS = 600
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#CACHE_MIDDLEWARE_KEY_PREFIX = 'books_progopedia_com'
