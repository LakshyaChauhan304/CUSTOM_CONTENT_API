from rest_framework import serializers
from django.contrib.auth import get_user_model




class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data.get('first_name', ''),
        last_name=validated_data.get('last_name', ''),
        password=validated_data['password']
        user = get_user_model()
        new_user = user.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return new_user