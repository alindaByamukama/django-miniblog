from django.db import models

# Create your models here.
class Users(models.Model):
    # userID = models.IntegerField()
    username = models.TextField()
    email = models.EmailField()
    # password = models.
