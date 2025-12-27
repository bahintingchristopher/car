"""
WSGI config for finalsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalsite.settings')

application = get_wsgi_application()



User = get_user_model()
# This creates a user named 'admin' with password 'password123' if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'bahintingchristopher', 'Christoff12!')


# import os
# from django.contrib.auth import get_user_model

# # Only run this if we are on Render
# if os.environ.get('RENDER'):
#     User = get_user_model()
#     if not User.objects.filter(username='admin').exists():
#         User.objects.create_superuser(
#             username='admin',
#             email='admin@example.com',
#             password='YourSecretPassword123' # Change this to a real password!
#         )
#         print("Superuser 'admin' created successfully.")