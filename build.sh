#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files
python manage.py collectstatic --no-input

# 3. Run migrations
python manage.py migrate

# 4. Create Admin (Superuser)
python manage.py shell -c "import os; from django.contrib.auth.models import User; u = os.environ.get('SUPERUSER_NAME'); e = os.environ.get('SUPERUSER_EMAIL'); p = os.environ.get('SUPERUSER_PASSWORD'); User.objects.filter(username=u).exists() or User.objects.create_superuser(u, e, p)"

# 5. Create Guest (Regular User)
python manage.py shell -c "import os; from django.contrib.auth.models import User; u = os.environ.get('GUEST_USER_NAME'); e = os.environ.get('GUEST_USER_EMAIL'); p = os.environ.get('GUEST_USER_PASSWORD'); User.objects.filter(username=u).exists() or User.objects.create_user(u, e, p)"