from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import DemoPage, ContentItem

User = get_user_model()

# ------------------------------
# User Registration Serializer
# ------------------------------
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'password'
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            password=validated_data['password']
        )
        return user


# ------------------------------
# Demo Page Serializer
# ------------------------------
class DemoPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoPage
        fields = [
            'id',
            'title',
            'subtitle',
            'body'
        ]


# ------------------------------
# Content Item Serializer
# ------------------------------
class ContentItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ContentItem
        fields = ['id', 'title', 'body', 'created_at', 'updated_at', 'status', 'user', 'user_username']
