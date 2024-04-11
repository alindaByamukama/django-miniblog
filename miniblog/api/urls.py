from django.urls import path
from .views import APIRoot, BlogPostViewSet, UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = format_suffix_patterns([
    path('', APIRoot),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='user-detail'),
    path('blogposts/', blogpost_list, name='blogpost-list'),
    path('blogposts/<int:pk>', blogpost_detail, name='blogpost-detail'),
    path('blogposts/(?P<title>.+)/$:', blogpost_filter, name='blogpost-filter')
])