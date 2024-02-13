from config.celery import app
from .send_email import send_confirmation_email, send_password_reset_email

@app.task
def send_confirmation_email_task(email, code):
    send_confirmation_email(email, code)
@app.task
def send_password_reset_task(email, user_id):
    send_password_reset_email(email, user_id)
