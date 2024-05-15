from django.db import models

# Create your models here.

# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

    # for user in User.objects.all():
    #     Token.objects.get_or_create(user=user)
    
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey('auth.User', related_name='blogposts', on_delete=models.RESTRICT, null=True)
    
    def __str__(self):
        return self.title