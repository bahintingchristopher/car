#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files
python manage.py collectstatic --no-input

# 3. Run migrations
python manage.py migrate

# 4. Create/Update Admin
python manage.py shell -c "from django.contrib.auth.models import User; import os; u=os.environ.get('SUPERUSER_NAME'); e=os.environ.get('SUPERUSER_EMAIL'); p=os.environ.get('SUPERUSER_PASSWORD'); user, created = User.objects.get_or_create(username=u, defaults={'email': e}); user.set_password(p); user.is_staff=True; user.is_superuser=True; user.save(); print(f'>>> ADMIN STATUS: User {u} is ready')"

# 5. Create Guest (As Staff so they can log in, but NOT superuser)
python manage.py shell -c "from django.contrib.auth.models import User; import os; u=os.environ.get('GUEST_USER_NAME'); e=os.environ.get('GUEST_USER_EMAIL'); p=os.environ.get('GUEST_USER_PASSWORD'); user, created = User.objects.get_or_create(username=u, defaults={'email': e}); user.set_password(p); user.is_staff=True; user.is_superuser=False; user.save(); print('>>> GUEST STATUS: Guest user ready')"

# 6. Automate View-Only Group and Assign Guest
python manage.py shell -c "from django.contrib.auth.models import User, Group, Permission; import os; group, _ = Group.objects.get_or_create(name='Viewers'); perms = Permission.objects.filter(codename__contains='view'); group.permissions.set(perms); u_name=os.environ.get('GUEST_USER_NAME'); user = User.objects.get(username=u_name); user.groups.add(group); print('>>> PERMISSIONS: Guest assigned to Viewers group')"

# 7. Load Car Data (Keep this at the end)
python manage.py load_car_data