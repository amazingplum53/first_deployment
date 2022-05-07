

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2-binary',
        'NAME': 'first',
        'USER': 'first',
        'PASSWORD': 'meatballs',
        'HOST': 'localhost',
        'PORT': '',
    }
}



# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True