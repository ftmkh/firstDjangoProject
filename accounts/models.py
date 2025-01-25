
'''from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.TextField(max_length=250, unique=True)
    password = models.CharField(max_length=300)
    email = models.EmailField(unique=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.username
'''