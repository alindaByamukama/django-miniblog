from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'blogposts', views.BlogPostViewSet, basename='blogpost')
router.register(r'users', views.UserViewSet, basename='user')
# router.register(r'register', views.UserRegistrationViewSet, basename='registration')
# router.register(r'login', views.UserLoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]