from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import BlogPost

class BlogPostViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(usernmae='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.blog_post = BlogPost.objects.create(title='Test Post', content='Tests Content', author=self.user)
        self.url = reverse('blogpost-detail', args=[self.blog_post.id])

    def test_get_blog_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')

    def test_create_blog_post(self):
        data = {'title': 'New Post', 'content': 'New Content', 'author': self.user.id}
        response = self.client.post(reverse('blogpost-list'), data, format='json' )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Post')