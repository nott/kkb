# -*- coding: utf-8 -*-
# Django settings for testproj project.

import os.path

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SITE_URL = 'http://kina.klu.by'
SITE_NAME = u'кіна.клу.бы / мінска'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2',
                                               # 'postgresql', 'mysql',
                                               # 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file 
                                         # if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost.
                                         # Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default.
                                         # Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Minsk'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'be'

LOCALE_PATHS = (os.path.join(PROJECT_ROOT, 'localecustom'),)
FORMAT_MODULE_PATH = 'formats'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/site_media/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/site_media/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/site_media/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'site_static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'alfptgy$mazte723vmiw#%b75oc@=lt@pif9(yflmtoco6uuh&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.static",
    "commonutils.social.context_processors.socialize_user"
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'commonutils.social.middleware.SocialAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.comments',

    'raven.contrib.django',
    'south',
    'debug_toolbar',

    'imagekit',
    'social_auth',

    'feedback',
    'blog',
    'commonutils.ncomments',
    'cinemaclubs',
)

COMMENTS_APP = 'commonutils.ncomments'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'sentry': {
            'level': 'DEBUG',
            'class': 'raven.contrib.django.handlers.SentryHandler',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

PYRES_DEFAULT_QUEUE = 'kinakluby'
FEEDBACK_QUEUE = PYRES_DEFAULT_QUEUE

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth_extra_services.vkontakte.VKontakteOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_IMPORT_BACKENDS = (
    'social_auth_extra_services',
)
DEFAULT_SOCIAL_AVATAR =  STATIC_URL + 'img/default_avatar.png'
SOCIAL_AUTH_SESSION_EXPIRATION = False
SOCIAL_AUTH_ERROR_KEY = 'SOCIAL_AUTH_ERROR_KEY'

LOGIN_URL          = '/minska/'
LOGIN_REDIRECT_URL = '/minska/'
LOGIN_ERROR_URL    = '/auth-error/'

TWITTER_CONSUMER_KEY = ''  # please define in settings_local
TWITTER_CONSUMER_SECRET= ''  # please define in settings_local
TWITTER_EXTRA_DATA = [('screen_name', 'screen_name')]

FACEBOOK_APP_ID = ''  # please define in settings_local
FACEBOOK_API_SECRET = ''  # please define in settings_local

VKONTAKTE_APP_ID = ''  # please define in settings_local
VKONTAKTE_APP_SECRET = ''  # please define in settings_local
VKONTAKTE_APP_AUTH = 1

AVATARIZATOR_URL = 'http://avatr.nott.cc/%(provider)s/%(uid)s?key=%(key)s'
AVATARIZATOR_KEY = 'secret'

# for django debug toolbar
INTERNAL_IPS = ('127.0.0.1',)

# keys for publishing as a twitter bot
PUBLISHING_TWITTER_CONSUMER_KEY = ''  # please define in settings_local
PUBLISHING_TWITTER_CONSUMER_SECRET = ''  # please define in settings_local
PUBLISHING_TWITTER_ACCESS_KEY = ''  # please define in settings_local
PUBLISHING_TWITTER_ACCESS_SECRET = ''  # please define in settings_local

PUBLISHING_FACEBOOK_ACCESS_TOKEN = ''  # please define in settings_local
PUBLISHING_FACEBOOK_PAGE_ID = ''  # please define in settings_local

PUBLISHING_VKONTAKTE_USER = ()  # please define in settings_local
PUBLISHING_VKONTAKTE_REPOST_USERS = {}  # please define in settings_local

PUBLISHING_LJ_TARGETS = {}  # {target_key: (username, md5_pwd_hash.hexdigest,
                            #               extra_params_dict)}

try:
    from settings_local import *
except ImportError:
    pass
