"""
Production settings for mogak-us project.
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "your-production-secret-key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["your-production-domain.com"]

# django-vite settings
DJANGO_VITE_DEV_MODE = DEBUG  # follow Django's dev mode
