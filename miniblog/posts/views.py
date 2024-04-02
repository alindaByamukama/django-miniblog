from django.shortcuts import render
from .models import BlogPost
from rest_framework import generics
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # blogpost id
    lookup_field = "pk"

def posts_list(request):
    posts = BlogPost.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

# def post_page(request, slug):
#     post = BlogPost.objects.get(slug=slug)
#     return render(request, 'posts/post_page.html', {'post': post})