from rest_framework import permissions, viewsets, filters
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import BlogPost
from .serializers import BlogPostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class APIRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('user-list', request=request, format=format),
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

# class UserRegistrationViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

# class UserLoginViewSet(viewsets.ModelViewSet):
#     def post(self, request):
#         user = authenticate(username=request.data['username'], password=request.data['password'])
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=401)