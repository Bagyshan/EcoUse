from django.core.mail import send_mail
from django.utils.html import format_html

def send_confirmation_email(email, code):
    activation_url = f'http://localhost:3000/account/activate/?u={code}'
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
