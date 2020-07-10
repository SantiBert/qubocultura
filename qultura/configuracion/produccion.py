from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = ['qubo.pythonanywhere.com','www.qubocultura.com','qubocultura.com']
=======
ALLOWED_HOSTS = ['qubo.pythonanywhere.com','www.qubocultura.com']
>>>>>>> faccff3d2e4aaaa3a7bf91f10e0eefe13563fa5a


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qubo$default',
        'USER': 'qubo',
        'PASSWORD': 'amantedelacomida',
        'HOST': 'qubo.mysql.pythonanywhere-services.com',
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
