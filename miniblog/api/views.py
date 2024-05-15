from rest_framework import permissions, viewsets, filters, authentication
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import BlogPost
from .serializers import BlogPostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class APIRoot(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        current_user = request.User
        return Response({
            'username': current_user.username,
            'posts': current_user.posts
        })

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

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