from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('blogposts/details/<int:pk>', views.BlogPostRetrieve.as_view(), name='blogpost-retrieve'),
    path('blogposts/<int:pk>', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-update'),
    path('blogposts/filter/', views.BlogPostListFilter.as_view(), name='blogpost-filter')
])