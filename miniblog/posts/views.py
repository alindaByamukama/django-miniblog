from django.shortcuts import render
from .models import BlogPost
from rest_framework import generics
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.obejcts.all()
    serializer_class = BlogPostSerializer

def posts_list(request):
    blog_posts = BlogPost.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': blog_posts})

def post_page(request, slug):
    blog_post = BlogPost.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': blog_post})