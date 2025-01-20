import os
from pathlib import Path

from dotenv import load_dotenv

__all__ = ()

load_dotenv()


def env_validator(env: str):
    return env.lower() in ["true", "yes", "1", "y", "t"]


SECRET_KEY = os.getenv(
    "DJANGO_CTF_SECRET_KEY",
    "django-insecure-g^_9#0r_apxp3u27(sbh$-67hmm6mu1u5x0%eto309@091)!b-",
)

ENCRYPTION_KEY = os.getenv(
    "DJANGO_CTF_ENCRYPTION_KEY",
    "dsEa3e6lF983WPH88NsSS9A0HGCIK5xA",
).encode()

DEBUG = env_validator(os.getenv("DJANGO_CTF_DEBUG", "true"))

ALLOWED_HOSTS = os.getenv("DJANGO_CTF_ALLOWED_HOSTS", "127.0.0.1").split(
    ","
)

CSRF_TRUSTED_ORIGINS = [f"https://{x}" for x in ALLOWED_HOSTS]

BASE_DIR = Path(__file__).resolve().parent.parent

SITE_URL = os.getenv("DJANGO_CTF_SITE_URL", "http://127.0.0.1:8080")

AUTH_USER_MODEL = "users.User"
# Application definition

INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
    "main",
    "web_tasks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DJANGO_CTF.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

STATIC_ROOT = BASE_DIR / "static"

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_URL = "/static/"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

WSGI_APPLICATION = "DJANGO_CTF.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "CTF.sqlite3",
#     }
# }

DB_NAME = os.getenv("DJANGO_CTF_POSTGRESQL_NAME", "CTF")
DB_USER = os.getenv("DJANGO_CTF_POSTGRESQL_USER", "postgres")
DB_PASSWORD = os.getenv("DJANGO_CTF_POSTGRESQL_PASSWORD", "root")
DB_HOST = os.getenv("DJANGO_CTF_POSTGRESQL_HOST", "localhost")
DB_PORT = int(os.getenv("DJANGO_CTF_POSTGRESQL_PORT", "5432"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    },
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"