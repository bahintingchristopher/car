import os  # Standard Python tool to interact with the Operating System (folders, environment variables)
from pathlib import Path  # Modern tool for handling file paths easily
import dj_database_url  # Special tool to connect to Render's PostgreSQL database automatically

# Calculates the main folder of my project so Django knows where to find everything
BASE_DIR = Path(__file__).resolve().parent.parent

# The "Password" for my website. It uses a secret key from Render or a fake one for testing
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-test-key-only')

# Security: False means "Production Mode" (Safe); True means "Development Mode" (Shows errors)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Lists which websites are allowed to display my app (Localhost for testing, Render for live)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'car-store-sfnj.onrender.com']

# --- APPS LIST ---
INSTALLED_APPS = [
    'cloudinary_storage',         # Manages sending images to Cloudinary (Must be at the top)
    'django.contrib.admin',       # The built-in /admin dashboard
    'django.contrib.auth',        # Handles users and passwords
    'django.contrib.contenttypes',# Internal Django requirement
    'django.contrib.sessions',    # Keeps users logged in while they browse
    'django.contrib.messages',    # Handles pop-up "success/error" notifications
    'django.contrib.staticfiles', # Manages CSS and JavaScript files
    'cloudinary',                 # The base Cloudinary SDK (Must be here for image fields to work)
    'car',                        # my APP: where my cars and models are kept
]

# --- SECURITY & UTILITY MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Basic security protections
    'whitenoise.middleware.WhiteNoiseMiddleware',     # Efficiently serves CSS/JS files on Render
    'django.contrib.sessions.middleware.SessionMiddleware', # Connects sessions to users
    'django.middleware.common.CommonMiddleware',      # Handles URLs (like adding slashes)
    'django.middleware.csrf.CsrfViewMiddleware',      # Protects forms from hackers
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Links users to requests
    'django.contrib.messages.middleware.MessageMiddleware', # Allows sending messages to users
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Prevents site from being used in frames
]

# Tells Django where the main URL routes file is
ROOT_URLCONF = 'finalsite.urls'

# Configures how my HTML files are processed
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],             # can add extra folders for HTML here
        'APP_DIRS': True,       # Looks inside each app (like 'car') for a /templates/ folder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Connects the web server (like Gunicorn) to my code
WSGI_APPLICATION = 'finalsite.wsgi.application'

# --- THE DATABASE ---
DATABASES = {
    'default': dj_database_url.config(
        # Uses DATABASE_URL on Render (Postgres) or SQLite on our laptop
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600 # Keeps the connection open for speed
    )
}

# Standard security checks to make sure user passwords aren't too simple
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Sets the language and time zone (UTC is standard for servers)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES (CSS/JS) ---
STATIC_URL = '/static/' 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Where CSS files go when deployed

# --- MEDIA FILES (TEMPORARY LOCAL STORAGE) ---
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# --- RENDER-SPECIFIC SECURITY ---
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # Fixes HTTPS issues on Render
SESSION_COOKIE_SECURE = True   # Only sends session cookies over HTTPS
CSRF_COOKIE_SECURE = True      # Only sends CSRF cookies over HTTPS
CSRF_TRUSTED_ORIGINS = ['https://car-store-sfnj.onrender.com'] # Allows Render to submit forms

# --- CLOUDINARY (PERMANENT IMAGE STORAGE) ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'), # From my Cloudinary Dashboard
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),     # From my Cloudinary Dashboard
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET') # From my Cloudinary Dashboard
}

# --- NEW STORAGE CONFIGURATION FOR DJANGO 6.0 ---
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "cloudinary_storage.storage.StaticCloudinaryStorage",
    },
}