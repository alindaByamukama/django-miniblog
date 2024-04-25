from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api import views

router = DefaultRouter()
router.register(r'blogposts', views.BlogPostViewSet, basename='blogpost')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('', include(router.urls)),
]