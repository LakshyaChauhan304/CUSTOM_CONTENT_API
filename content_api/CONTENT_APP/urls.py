from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    register_user,
    login_view,
    login_user,
    logout_view,
    DemoPageViewSet,
    ContentItemViewSet,
    signup,
    home,
    items_list,
    add_item,
    
)

router = DefaultRouter()
router.register(r'demo', DemoPageViewSet, basename='demo')
router.register(r'items', ContentItemViewSet, basename='items')

urlpatterns = [
    # Django UI views for Option A
    path("signup/", signup, name="signup"),
    path("", home, name="home"),
    path("items/", items_list, name="items_list"),
    path("add-item/", add_item,name = "add_item"),


    # API routes
    path("register/", register_user, name="register"),
    path("login/", login_view, name="login"),
    path("api/login/", login_user, name="api_login"),
    path("logout/", logout_view, name="logout"),
    path("api/", include(router.urls)),
]
