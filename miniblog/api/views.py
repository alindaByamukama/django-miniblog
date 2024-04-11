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

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self, serializer):
        # return a list of blog posts by title
        title = self.kwargs['title']
        return BlogPost.objects.filter(blogpost__title=title)