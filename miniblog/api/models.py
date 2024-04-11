from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey('auth,User', related_name='blogposts', on_delete=models.RESTRICT, null=True)
    
    def __str__(self):
        return self.title