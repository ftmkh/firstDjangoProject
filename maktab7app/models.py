from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(default='default.png')
    author = models.CharField(max_length=250)
    created_at = DateTimeField(default=timezone.now , editable=False)
    login_require = models.BooleanField(default=False)
    published_date = DateTimeField(default=timezone.now )
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title



    class Meta:

        ordering =['-published_date']