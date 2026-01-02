#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files
python manage.py collectstatic --no-input

# 3. Run migrations
python manage.py migrate

# 4. Create/Update Admin (The Fail-Safe Way)
python manage.py shell -c "from django.contrib.auth.models import User; import os; \
username = os.environ.get('SUPERUSER_NAME'); \
email = os.environ.get('SUPERUSER_EMAIL'); \
password = os.environ.get('SUPERUSER_PASSWORD'); \
user, created = User.objects.get_or_create(username=username, defaults={'email': email}); \
user.set_password(password); \
user.is_staff = True; \
user.is_superuser = True; \
user.save(); \
print('ADMIN USER UPDATED/CREATED SUCCESSFULLY')"

# 5. Create Guest (Regular User)
python manage.py shell -c "import os; from django.contrib.auth.models import User; u = os.environ.get('GUEST_USER_NAME'); e = os.environ.get('GUEST_USER_EMAIL'); p = os.environ.get('GUEST_USER_PASSWORD'); User.objects.filter(username=u).exists() or User.objects.create_user(u, e, p)"