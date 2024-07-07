from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    published = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("auth.User", related_name="blogposts", on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published']