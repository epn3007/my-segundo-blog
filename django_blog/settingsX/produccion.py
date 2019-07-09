from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['epn3007.mysql.pythonanywhere-services.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'epn3007',
        'PASSWORD': '',
        'HOST': 'epn3007.mysql.pythonanywhere-services.com',
        'PORT': '3306',    }
}


#STATICFILES_DIRS=(BASE_DIR,'static')