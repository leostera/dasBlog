# Import project settings
from blog.settings import *
# And override them

# Set debug to true
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Change main urls file
ROOT_URLCONF = 'dev.urls'

# so that "python manage.py test" invokes django-nose-selenium
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# should match SELENIUM_URL_ROOT which defaults to http://127.0.0.1:8000
LIVE_SERVER_PORT = 8000

# Reconfigure the database
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3', 
        # Or path to database file if using sqlite3.
        'NAME': full_path('dasblog.db'), 
        # Not used with sqlite3.                     
        'USER': '',                      
        # Not used with sqlite3.
        'PASSWORD': '',                  
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',                      
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',                      
        # Path to test database file if using sqlite3.
        'TEST_NAME': full_path('dasblog.test.db'),                      
    }
}

# Recalculate media path
MEDIA_ROOT = full_path("public/media")

# Override static files dir with recalculated static path
STATICFILES_DIRS = (
    full_path('public/static'),
)

# Add 'django_nose' to the installed applications.
INSTALLED_APPS += (
    # Testing
    'django_nose',
)