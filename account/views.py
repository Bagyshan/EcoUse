from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import RegisterSerializer, LogOutSerializer
from .send_email import send_confirmation_email
from django.shortcuts import get_object_or_404

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_confirmation_email(user.email, user.activation_code)

class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data['refresh']
        try:
            RefreshToken(refresh_token).blacklist()
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Вы успешно вышли из системы.'}, status=status.HTTP_200_OK)

class ActivationView(APIView):
    def post(self, request):
        activation_code = request.data.get('activation_code')
        if not activation_code:
            return Response({
                'error': 'Нужен код активации'
            }, 404)
        user = get_object_or_404(CustomUser, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        try:
            send_confirmation_email(user.email, user.activation_code)
            return Response({
                'message': 'Пользователь активирован'}, 200
            )
        except Exception as e:
            return Response(
                {'error': f'Ошибка при отправке подтверждения по электронной почте: {e}'},
                            500
            )