from django.db import models
from maktab7app.models import Post

# Create your models here.
class Comments(models.Model):
    author = models.CharField(max_length=250)
    body = models.TextField()
    post = models.ForeignKey(Post,related_name='comments',
<<<<<<< HEAD
                             on_delete=models.CASCADE)
    subject =models.CharField(max_length=250)
=======
                             on_delete=models.CASCADE , null=True)
    email = models.EmailField(null=True, blank=True)  # Allow null values initially
    name = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)  # Optional field
    body = models.TextField(null=True, blank=True)  # Optional field
>>>>>>> 7f47bf3287eead18b8bd39d3c9ded968cf1be8e5
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    approved = models.BooleanField(default=False)