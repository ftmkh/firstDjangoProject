from django.db import models
from maktab7app.models import Post

# Create your models here.
class Comments(models.Model):
    author = models.CharField(max_length=250)
    body = models.TextField()
    post = models.ForeignKey(Post,related_name='comments',
                             on_delete=models.CASCADE)
    subject =models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    approved = models.BooleanField(default=False)