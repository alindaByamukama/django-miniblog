from django.db import models
from users.models import Users

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Users, null=True, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.title} by {self.user.username} at {self.date}"