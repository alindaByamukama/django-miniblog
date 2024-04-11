from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from django.contrib.auth.models import User

from .models import BlogPost
from .serializers import BlogPostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class APIRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('user-list',request=request, format=format),
            'posts': reverse('blogpost-detail', request=request, format=format)
        })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # list and retrieve 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlogPostList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostRetrieve(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class BlogPostListFilter(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        # get title from query params or default to empty string
        title = request.query_params.get('title', '')

        if title:
            # filter the queryset based on the title
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            # if no title is provided return all blog posts
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)