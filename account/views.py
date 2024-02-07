from http import HTTPStatus

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer , LogOutSerializer
from django.contrib.auth import get_user_model
from .send_email import send_confirmation_email
from django.shortcuts import get_object_or_404
from .tasks import send_confirmation_email_task
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


User = get_user_model()

class RegistrationView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email_task.delay(user.email, user.activation_code)
            except:
                return Response(
                    {
                        'message': 'Письмо с кодом активации небыло отправлено на почту',
                        'data': serializer.data
                    }, status=HTTPStatus.CREATED
                )
            return Response(serializer.data, status=HTTPStatus.CREATED)


class ActivationView(APIView):
    def get(self, request):
        activation_code = request.data.get('activation_code')
        if not activation_code:
            return Response({
                'error': 'Нужен код активации'
            }, status=HTTPStatus.BAD_REQUEST)
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        try:
            send_confirmation_email(user.email, user.activation_code)
            return Response({
                'message': 'Пользователь активирован'}, status=HTTPStatus.OK
            )
        except Exception as e:
            return Response(
                {'error': f'Ошибка при отправке подтверждения по электронной почте: {e}'},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
        
class LogoutView(APIView):
    serializer_class = LogOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response('Успешно разлогинились', 200)


# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import CustomUser, PasswordResetCode
# from .serializers import PasswordResetSerializer
# from .tasks import send_password_reset_email_task
# from django.utils.crypto import get_random_string

# class PasswordResetView(APIView):
#     serializer_class = PasswordResetSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data.get('email')
#             user = get_object_or_404(CustomUser, email=email)

#             # Создаем уникальный код для сброса пароля
#             reset_code = get_random_string(length=32)

#             # Сохраняем код в базе данных, связывая его с пользователем
#             PasswordResetCode.objects.create(user=user, code=reset_code)

#             # Отправляем электронное письмо с кодом сброса пароля
#             send_password_reset_email_task.delay(user.email)

#             return Response({'message': 'Письмо с инструкциями по сбросу пароля отправлено на ваш адрес электронной почты.'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
