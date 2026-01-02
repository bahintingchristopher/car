#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files
python manage.py collectstatic --no-input

# 3. Run migrations
python manage.py migrate

# 4. Create/Update Admin (One single line for safety)
python manage.py shell -c "from django.contrib.auth.models import User; import os; u=os.environ.get('SUPERUSER_NAME'); e=os.environ.get('SUPERUSER_EMAIL'); p=os.environ.get('SUPERUSER_PASSWORD'); user, created = User.objects.get_or_create(username=u, defaults={'email': e}); user.set_password(p); user.is_staff=True; user.is_superuser=True; user.save(); print(f'>>> ADMIN STATUS: User {u} is ready')"

# 5. Create Guest User (One single line)
python manage.py shell -c "from django.contrib.auth.models import User; import os; u=os.environ.get('GUEST_USER_NAME'); e=os.environ.get('GUEST_USER_EMAIL'); p=os.environ.get('GUEST_USER_PASSWORD'); User.objects.filter(username=u).exists() or User.objects.create_user(u, e, p); print('>>> GUEST STATUS: Guest user ready')"