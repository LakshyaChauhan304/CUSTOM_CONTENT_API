from django.contrib.auth import authenticate
from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from .models import DemoPage, ContentItem
from .serializers import (
    UserRegistrationSerializer,
    DemoPageSerializer,
    ContentItemSerializer,
)


# --------------------------
# User Registration
# --------------------------
@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # optional: create token automatically
        Token.objects.get_or_create(user=user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------------
# Login API
# --------------------------
@api_view(['POST'])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "username and password required"}, status=400)

    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username})

    return Response({"error": "Invalid credentials"}, status=400)


# --------------------------
# Demo Page API (Wagtail Pages)
# --------------------------
class DemoPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DemoPage.objects.live().public()
    serializer_class = DemoPageSerializer
    permission_classes = [AllowAny]


# --------------------------
# Content Item API (CRUD)
# --------------------------
class ContentItemViewSet(viewsets.ModelViewSet):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer

# --------------------------
# UI Views (HTML pages)
# --------------------------

def ui_register(request):
    return render(request, "CONTENT_APP/register.html")

def ui_login(request):
    return render(request, "CONTENT_APP/login.html")

def ui_items(request):
    return render(request, "CONTENT_APP/items.html")

def ui_add_item(request):
    return render(request, "CONTENT_APP/add_item.html")

