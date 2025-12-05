from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout 
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm,LoginForm,ContentItemForm

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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# --------------------------
# UI Views (HTML pages)
# --------------------------

def home(request):
    return render(request,"CONTENT_APP/home.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect("items_list")

    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request,"CONTENT_APP/signup.html",{"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("items_list")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data["username_or_email"]
            password = form.cleaned_data["password"]

            User = get_user_model()
            user = None

            if User.objects.filter(username=identifier).exists():
                user = authenticate(request, username=identifier, password=password)
            elif User.objects.filter(email=identifier).exists():
                try:
                    username = User.objects.get(email=identifier).username
                    user = authenticate(request, username=username, password=password)
                except User.MultipleObjectsReturned:
                     form.add_error(None, "Multiple users with this email found.")

            if user:
                auth_login(request, user)
                return redirect("items_list")
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, "CONTENT_APP/login.html", {"form": form})

def logout_view(request):
    auth_logout(request)
    return redirect("home")


def items_list(request):
    items = ContentItem.objects.all().select_related("user")
    return render(request, "CONTENT_APP/items.html", {"items": items})

@login_required
def add_item(request):
    if request.method == "POST":
        form = ContentItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect("items_list")

    else:
        form = ContentItemForm()

    return render(request, "CONTENT_APP/add_item.html", {"form": form})

@login_required
def edit_item(request, pk):
    try:
        item = ContentItem.objects.get(pk=pk, user=request.user)
    except ContentItem.DoesNotExist:
        return redirect("items_list")

    if request.method == "PUT":
        import json
        data = json.loads(request.body)
        item.title = data.get("title", item.title)
        item.body = data.get("body", item.body)
        item.status = data.get("status", item.status)
        item.save()
        return JsonResponse({"message": "Item updated successfully"})
    
    if request.method == "GET" and request.headers.get('content-type') == 'application/json':
        return JsonResponse({
            "title": item.title,
            "body": item.body,
            "status": item.status
        })

    return render(request, "CONTENT_APP/edit_item.html", {"item": item})

@login_required
def work_list(request):
    items = ContentItem.objects.filter(user=request.user, status='completed').order_by('-updated_at')
    return render(request, "CONTENT_APP/work.html", {"items": items})

from django.http import JsonResponse
