from django.db import models
from maktab7app.models import Post

# Create your models here.
class Comments(models.Model):
    post = models.ForeignKey(Post,related_name='comments',
                             on_delete=models.CASCADE)
    subject =models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)