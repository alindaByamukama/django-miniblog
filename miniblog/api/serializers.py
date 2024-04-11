from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published', 'author']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='blogpost-retrieve', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'posts']