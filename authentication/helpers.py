from django.conf import settings
from django.core.mail import send_mail


def send_email(user=None, email=None, message=None, subject=None):
    subject = subject or "Wellcome mail"
    msg = message or f"Wellcome Mr/Ms {user.email}."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    try:
        send_mail(subject, msg, email_from, recipient_list)
    except Exception:
        pass


def send_sms(otp=None, message=None):
    msg = f"Your login otp is {otp}."
    if message is not None:
        msg = message
    print(msg)
