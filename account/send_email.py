from base64 import urlsafe_b64encode
from django.core.mail import send_mail
from django.utils.html import format_html

def send_confirmation_email(email, code):
    activation_url = f'http://35.232.206.28/account/activate/{code}'
    message = format_html(
        'Здравствуйте, активируйте ваш аккаунт'
        '<br>'
        'Чтобы активировать аккаунт, перейдите по ссылке:'
        '<br>'
        '<a href="{}">{}</a>'
        '<br>'
        'Не передавайте код никому',
        activation_url, activation_url
    )


    try:
        send_mail(
        'Здравствуйте',
        message,
        'test@gmail.com',
        [email],
        fail_silently=False
    )
    except Exception as e:
        print(f"Ошибка при отправке электронной почты: {e}")


def send_password_reset_email(email, user_id):
    password_reset_url = f'http://35.232.206.28/account/password_confirm/{user_id}'
    message = format_html(
        'Здравствуйте, вот ваш код:'
        '<br>'
        '<a href="{}">{}</a>'
        '<br>',
        password_reset_url,
        user_id
    )




    send_mail(
        'Здравствуйте',
        message,
        'test@gmail.com',
        [email],
        fail_silently=False
    )

