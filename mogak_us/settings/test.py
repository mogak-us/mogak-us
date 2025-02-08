"""
Test settings for mogak-us project.
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "test-secret-key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Use PostgreSQL for tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_your_db_name",
        "USER": "your_db_user",
        "PASSWORD": "your_db_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# django-vite settings
DJANGO_VITE_DEV_MODE = DEBUG  # follow Django's dev mode
