from .send_email import send_confirmation_email
from celery import shared_task
from config.celery import app

@shared_task
def send_confirmation_email_task(email, code):
    send_confirmation_email(email, code)