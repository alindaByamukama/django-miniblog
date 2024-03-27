from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User)

    def __str__(self):
        return self.title
        # return f"Post by {self.user.username} at {self.date}"
    