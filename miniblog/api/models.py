from django.db import models
from django.conf import settings
# auto generate tokens for users
from django.db.models import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey('auth.User', related_name='blogposts', on_delete=models.RESTRICT, null=True)
    
    def __str__(self):
        return self.title