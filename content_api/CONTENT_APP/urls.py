from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import DemoViewSet, register_user

router = DefaultRouter()
router.register(r'demo', DemoViewSet, basename='demo')

urlpatterns = [
    path("register_user", views.register_user, name="register_user")
    path("api/", include(router.urls)),
]
