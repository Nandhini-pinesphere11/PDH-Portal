from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Domain

def send_renewal_alerts():
    today = datetime.now().date()
    one_week = timedelta(weeks=1)
    domains = Domain.objects.filter(due_date__lte=today + one_week, status='active')

    for domain in domains:
        subject = f'Renewal Alert: {domain.title}'
        message = render_to_string('renewal_alert_email.html', {'domain': domain})
        recipient_list = domain.notify.split(',')
        send_mail(subject, message, 'kiruthika@pinesphere.info', recipient_list)
