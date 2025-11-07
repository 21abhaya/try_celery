from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_mail_task(subject, message, from_email, recipient_list):
    """
    A celery task to send an email.
    """
    try:
        send_mail(
            subject, 
            message, 
            from_email, 
            recipient_list, 
            fail_silently=False
        )
    except Exception as e:
        print("Failed to send email due to this exception:", e)
