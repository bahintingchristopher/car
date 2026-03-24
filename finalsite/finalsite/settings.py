import os  # Standard Python tool to interact with the Operating System (folders, environment variables)
from pathlib import Path  # Modern tool for handling file paths easily
import dj_database_url  # Special tool to connect to Render's PostgreSQL database automatically

# Calculates the main folder of my project so Django knows where to find everything
BASE_DIR = Path(__file__).resolve().parent.parent

# The "Password" for my website. It uses a secret key from Render or a fake one for testing
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-only-key')

# Security: False means "Production Mode" (Safe); True means "Development Mode" (Shows errors)
DEBUG = False


# Lists which websites are allowed to display my app (Localhost for testing, Render for live)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'car-store-sfnj.onrender.com', 'bahinsCars.pythonanywhere.com']

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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

# --- STORAGE LOGIC: CLOUDINARY FOR LIVE, LOCAL FOR TESTING ---
if not DEBUG:
    # This runs on RENDER (Live Site)
    STORAGES = {
        "default": {
            "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
        },
        "staticfiles": {
            "BACKEND": "cloudinary_storage.storage.StaticCloudinaryStorage",
        },
    }
else:
    
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }

# --- CLOUDINARY (PERMANENT IMAGE STORAGE) ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET')
}

# --- THE END OF THE FILE ---