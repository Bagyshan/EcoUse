from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from .send_email import send_confirmation_email

# User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=10, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=10, required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'email', 'password', 'password_confirm', 'phone_number', 'status', 'username'
        ]

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(password=password, **validated_data)
        send_confirmation_email(user.email, user.activation_code)
        return user

class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True, write_only=True)

# from rest_framework import serializers

# class PasswordResetSerializer(serializers.Serializer):
#     email = serializers.EmailField()