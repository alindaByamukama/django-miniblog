from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost

# Create your tests here.
class BlogPostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        BlogPost.objects.create(title='Test Post', content='Test Content', author=user)

    def test_blog_post_content(self):
        post = BlogPost.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_content = f'{post.content}'
        self.assertEqual(expected_title, 'Test Post')
        self.assertEqual(expected_content, 'Test Content')