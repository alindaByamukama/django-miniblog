from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost

class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = BlogPost
        fields = ['url', 'id', 'title', 'content', 'published', 'author']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='blogpost-detail', read_only=True)
    password = serializers.Charfield(write_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'posts', 'password']