from rest_framework import generics, status, permissions, viewsets, filters
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

    # Example: http://127.0.0.1:8000/blogposts/?search=blog
    filter_backends = [filters.SearchFilter]
    search_fields = ['author__username', 'title']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })