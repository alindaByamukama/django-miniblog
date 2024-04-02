from django.db import models
from users.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User.username)

    def __str__(self):
        return self.title
        # return f"Post by {self.user.username} at {self.date}"