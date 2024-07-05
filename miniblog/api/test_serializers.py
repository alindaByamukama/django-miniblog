from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory
from .models import BlogPost
from .serializers import BlogPostSerializer, UserSerializer

class BlogPostSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.blog_post = BlogPost.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.request = APIRequestFactory().get('/')
        self.serializer = BlogPostSerializer(instance=self.blog_post, context={'request': self.request})

        def test_contains_expected_fields(self):
            data = self.serializer.data
            self.assertCountEqual(data.keys(), ['url', 'id', 'title', 'content', 'published', 'updated_at', 'author'])
        
        def test_author_field_content(self):
            data = self.serializer.data
            self.assertEqual(data['author'], self.user.username)

class UserSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.request = APIRequestFactory().get('/')
        self.serializer = UserSerializer(instance=self.user, context={'request': self.request})

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['url', 'username', 'email', 'posts'])

    def test_username_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.user.username)