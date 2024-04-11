from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users-list-create'),
    path('users/add', views.UserCreate.as_view(), name='users-create'),
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-update'),
    path('blogposts/filter/', views.BlogPostListFilter.as_view(), name='blogpost-filter')
]