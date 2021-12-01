import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cookbook.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import Profile

for user in User.objects.filter(profile__isnull=True):
    Profile.objects.create(user=user)