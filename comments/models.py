from django.db import models
from maktab7app.models import Post

# Create your models here.
class Comments(models.Model):
    post = models.ForeignKey(Post,related_name='comments',
                             on_delete=models.CASCADE , null=True)
    email = models.EmailField(null=True, blank=True)  # Allow null values initially
    name = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)  # Optional field
    body = models.TextField(null=True, blank=True)  # Optional field
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)