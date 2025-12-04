from django.contrib.auth import authenticate, login as auth_login 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm,LoginForm

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

def home(request):
    return render(request,"CONTENT_APP/home.html")

def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("ui_login")
    return render(request,"CONTENT_APP/signup.html",{"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data["username_or_email"]
            password = form.cleaned_data["password"]

            # Try username first
            from django.contrib.auth.models import User
            user = None

            if User.objects.filter(username=identifier).exists():
                user = authenticate(request, username=identifier, password=password)
            elif User.objects.filter(email=identifier).exists():
                username = User.objects.get(email=identifier).username
                user = authenticate(request, username=username, password=password)

            if user:
                login_view(request, user)
                return redirect("ui_items")  # or any page
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, "CONTENT_APP/login.html", {"form": form})


def items_list(request):
    items = ContentItem.objects.all().select_related("user")
    return render(request, "CONTENT_APP/items.html", {"items": items})
