from django.urls import path
from .views import APIRoot, BlogPostViewSet, UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = format_suffix_patterns([
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('blogposts/', views.BlogPostList.as_view(), name='blogpost-list'),
    path('blogposts/<int:pk>/details', views.BlogPostRetrieve.as_view(), name='blogpost-detail'),
    path('blogposts/filter/', views.BlogPostListFilter.as_view(), name='blogpost-filter')
])