from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"blogposts", views.BlogPostViewSet, basename="blogpost")
router.register(r"users", views.UserViewSet, basename="user")
# router.register(r"register", views.RegisterViewSet, basename="register")

urlpatterns = [
    path("", include(router.urls)),
]
