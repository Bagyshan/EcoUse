from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .send_email import send_confirmation_email
from .tasks import send_confirmation_email_task, send_password_reset_task
from .serializers import CustomPasswordConfirmSerializer, CustomResetPasswordResetSerializer, RegisterSerializer , LogOutSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from http import HTTPStatus


User = get_user_model()

class RegistrationView(APIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(request_body=RegisterSerializer)
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
        activation_code = self.request.query_params.get('u') 
        if not activation_code:
            return Response({
                'error': 'Нужен код активации'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()

        try:
            send_confirmation_email(user.email, user.activation_code)
            return Response({
                'message': 'Пользователь активирован'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': f'Ошибка при отправке подтверждения по электронной почте: {e}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class LogoutView(APIView):
    serializer_class = LogOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response('Успешно разлогинились', 200)


class CustomResetPasswordView(APIView):
    @swagger_auto_schema(request_body=CustomResetPasswordResetSerializer)
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.get(email=email)
        if not user:
            return Response({'ValidationError': 'Нет такого пользователя'}, status=HTTPStatus.BAD_REQUEST)
        user.create_activation_code()
        user.save()
        user_activation_code = user.activation_url
        send_password_reset_task.delay(email=email, user_id=user_activation_code)
        return Response('Вам на почту отправили сообщение', 200)
    

class CustomPasswordConfirmView(APIView):
    @swagger_auto_schema(request_body=CustomPasswordConfirmSerializer)
    def post(self, request, *args, **kwargs):
        new_password = request.data.get('new_password')
        password_confirm = request.data.get('password_confirm')
        user_id = self.kwargs.get('uidb64')
        user = User.objects.get(id=user_id)
        if new_password != password_confirm:
            return Response('Пароли не совпадают', 404)
        user.set_password(new_password)
        user.save()
        return Response('Ваш пароль изменен!', 201)
