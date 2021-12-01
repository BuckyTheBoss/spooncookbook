from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    image = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    common_recipes = models.ManyToManyField('main.Recipe')

