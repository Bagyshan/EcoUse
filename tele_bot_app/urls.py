from django.urls import path
from .views import TelegramBotView

urlpatterns = [
    path('webhook/', TelegramBotView.as_view(), name='telegram_webhook'),
]