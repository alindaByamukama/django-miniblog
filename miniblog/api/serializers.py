from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = BlogPost
        fields = ["url", "id", "title", "content", "published", "updated_at", "author"]


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=BlogPost.objects.all(), source='blogposts'
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["url", "username", "email", "posts", "password"]

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
# class RegisterSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only=True)

#     class Meta:
#         model = Userfields = ('username', 'email', 'password', 'password2')

#     def save(self, **kwargs):
#         user = User(
#             username=self.validated_data['username']
#             email=self.validated_data['email']
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#         if password != password2:
#             raise serializers.ValidationError({"password": "Passwords must match."})
#         user.set_password(password)
#         user.save()
#         return user