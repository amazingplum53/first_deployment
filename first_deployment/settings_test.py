
ALLOWED_HOSTS = ["ec2-3-9-16-89.eu-west-2.compute.amazonaws.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'first',
        'USER': 'first',
        'PASSWORD': 'meatballs',
        'HOST': 'localhost',
        'PORT': '',
    }
}



# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True