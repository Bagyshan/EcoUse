from .send_email import send_confirmation_email
from celery import shared_task
from config.celery import app

@app.task
def send_confirmation_email_task(email, code):
    send_confirmation_email(email, code)

# tasks.py

# from celery import shared_task
# from django.core.mail import send_mail
# from django.utils.html import format_html
# from .models import CustomUser, PasswordResetCode

# @shared_task
# def send_password_reset_email_task(email):
#     user = CustomUser.objects.get(email=email)

#     # Получаем последний созданный код сброса пароля пользователя
#     reset_obj = PasswordResetCode.objects.filter(user=user).latest('created_at')
#     reset_code = reset_obj.code

#     # Создаем URL для сброса пароля
#     reset_url = f'http://localhost:3000/account/reset-password/?code={reset_code}'

#     # Отправляем электронное письмо с инструкциями по сбросу пароля
#     message = format_html(
#         'Для восстановления пароля перейдите по ссылке:'
#         '<br>'
#         '<a href="{}">{}</a>'
#         '<br>'
#         'Не передавайте код никому',
#         reset_url, reset_url
#     )

#     try:
#         send_mail(
#             'Восстановление пароля',
#             message,
#             'noreply@example.com',  # Замените на ваш адрес отправителя
#             [email],
#             fail_silently=False,
#         )
#     except Exception as e:
#         print(f"Ошибка при отправке электронной почты: {e}")
