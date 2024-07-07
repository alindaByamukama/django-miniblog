import logging

from rest_framework import permissions, viewsets, filters
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from django.contrib.auth.models import User

from .models import BlogPost
from .serializers import BlogPostSerializer, UserSerializer, RegisterSerializer
from .permissions import IsAuthorOrReadOnly

logger = logging.getLogger(__name__)

# Create your views here.
class APIRoot(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "users": reverse("user-list", request=request, format=format),
                "posts": reverse("blogpost-detail", request=request, format=format),
            }
        )


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # list and retrieve
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-published')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # Example: http://127.0.0.1:8000/blogposts/?search=blog
    filter_backends = [filters.SearchFilter]
    search_fields = ["author__username", "title"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        logger.debug("Listing blog posts")
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.debug(f"Retrieving blog post with id: {kwargs.get('pk')}")
        return super().retrieve(request, *args, **kwargs)

class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)