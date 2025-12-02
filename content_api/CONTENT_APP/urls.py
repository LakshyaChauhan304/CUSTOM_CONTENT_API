from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    register_user,
    login_user,
    DemoPageViewSet,
    ContentItemViewSet,
    ui_register,
    ui_login,
    ui_items,
    ui_add_item,
)

router = DefaultRouter()
router.register(r'demo', DemoPageViewSet, basename='demo')
router.register(r'items', ContentItemViewSet, basename='items')

urlpatterns = [
    # UI routes
    path('ui/register/', ui_register, name='ui_register'),
    path('ui/login/', ui_login, name='ui_login'),
    path('ui/items/', ui_items, name='ui_items'),
    path('ui/add-item/', ui_add_item, name='ui_add_item'),

    # API routes
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('api/', include(router.urls)),
]
