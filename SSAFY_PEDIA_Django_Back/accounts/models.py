from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    # followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')