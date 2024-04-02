from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.Serializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "body", "slug", "date", "author"]