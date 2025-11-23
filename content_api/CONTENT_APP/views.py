from django.shortcuts import render
from CONTENT_APP.serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import DemoPage
from .serializers import DemoPageSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DemoPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DemoPage.objects.live().public()
    serializer_class = DemoPageSerializer
    permission_classes = [AllowAny]

