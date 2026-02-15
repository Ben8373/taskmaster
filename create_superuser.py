import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmaster.settings')
django.setup()

from django.contrib.auth.models import User

if User.objects.filter(username='Benjamin').exists():
    print("Superuser 'Benjamin' already exists!")
else:
    User.objects.create_superuser('Benjamin', 'benjaminc8373@gmail.com', 'I Love To Code')
    print("Superuser 'Benjamin' created successfully!")
