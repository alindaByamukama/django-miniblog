from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.Serializer):
    title = serializers.models.CharField(max_length=75)
    body = serializers.models.TextField()
    slug = serializers.models.SlugField()
    date = serializers.models.DateTimeField(auto_now_add=True)
    # author = serializers.models.ForeignKey(User)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.date = validated_data.get('date', instance.date)
        # instance.author = validated_data.get('author', instance.author)
        return instance