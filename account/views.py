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
    def post(self, request):
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