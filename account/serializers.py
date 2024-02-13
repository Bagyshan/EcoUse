from rest_framework import serializers
from .models import CustomUser
from .send_email import send_confirmation_email


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


class CustomResetPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = ['email']

class CustomPasswordConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=10, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=10, required=True, write_only=True)
    confirm_code = serializers.CharField(min_length=10, required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['new_password', 'password_confirm', 'confirm_code']
