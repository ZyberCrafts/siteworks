from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bmnv_zk1e(u&58_xq=af+$rncq@nze3t=*+kmwqyy94q1_15jq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'chatbot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'siteworks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'siteworks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'siteworks_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.brevo.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'festusonwonga@gmail.com'
EMAIL_HOST_PASSWORD = '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'

#payment

MPESA_ENVIRONMENT = 'sandbox'

# Credentials for the daraja app

# MPESA_CONSUMER_KEY = 'fK7TnqdWkc8AztAKGUGPBYSlQ3AH8o7nPkqRPDOENSzFIrT8'
# MPESA_CONSUMER_SECRET = '32rotjNmHNwh0hq1z0jQfmdJiAOBXArg4MxkTiDFLA5AbrLetjsNtVDm7osp9CiK'

MPESA_SHORTCODE = '600981'
MPESA_EXPRESS_SHORTCODE = '600981'
MPESA_SHORTCODE_TYPE = 'till_number'


# MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_USERNAME = 'austinnee'
MPESA_INITIATOR_SECURITY_CREDENTIAL = 'PEUFWSUDD9oAAfDc/dRcKVvs97q0qf3XSQEMBGPLWT1Q/u0b/6ZlhNSQo0116h' \
 'UUdQEcMnD8D8/j/63ClmUtdrvJzmmYiTK/yTEgRKcPDuBlwAquGa8IRycPJLXm+xyUk3iAc6WJkD2OWk/B/djDQTR86awXsznetr' \
 'gJkrFTROKeukLoPhak904AIVFiuHkWIkYGpjA5R/vMOwb6UFVIcdAESzTRfMjjLd7BSSC5poIh1mdxCnVCyGq7VL/1qw4p+ZRmz1' \
 '2e4M4DjKYDLP7hAaweHp3RpmGRyAr0HN/qwvQ3rJElzvZlVC18MKjh7sF7frezQOMjuOySIuJ4t+jnvw=='
