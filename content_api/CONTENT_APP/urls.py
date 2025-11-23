from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, DemoPageViewSet

router = DefaultRouter()
router.register(r'demo', DemoPageViewSet, basename='demo')

urlpatterns = [
    path('register/', register_user, name='register'),
    path("api/", include(router.urls)),
]
