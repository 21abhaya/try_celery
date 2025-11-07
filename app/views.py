from django.shortcuts import render
from django.conf import settings

from .tasks import send_mail_task



def check_if_divisible_by_5(value):
    if value % 5 == 0:
        return True


def test_view(request):
    value = request.POST.get('value', 1)
    if value:
        value = int(value)
    subject = "Tinkering around with Celery"
    message = f"This is a test email sent from a Celery task when the input value is {value}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = settings.DEFAULT_FROM_EMAIL.split(',')
    
    if check_if_divisible_by_5(value):
        send_mail_task.delay(
            subject,
            message,
            from_email,
            recipient_list
        )
            
    return render(request, 'test_view.html')

