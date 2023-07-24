from django.shortcuts import render, redirect,get_object_or_404
from .forms import DomainForm
from django.contrib import messages
from .models import Domain
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.urls import reverse
from django.utils.timezone import make_aware



from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from apphost.models import Hosting
from django.utils import timezone
from datetime import datetime, timedelta

from datetime import date
from django.utils.timezone import make_aware


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_renewal_alerts():
    today = datetime.now().date()
    one_day = timedelta(days=1)
    one_week = timedelta(weeks=1)
    one_month = timedelta(weeks=4)
    domains = Domain.objects.filter(due_date__lte=today + one_month, status='active')

    for domain in domains:
        # Send reminder 1 month before due date
        if domain.due_date <= today + one_month and domain.due_date > today + one_week + one_day:
            subject = f'Renewal Alert: {domain.title} - 1 month reminder'
            text_content = f'Dear {domain.domain_account},\n\nThis is a reminder that your domain {domain.title} is due for renewal in 1 month, on {domain.due_date}.\n\nPlease ensure that you renew your domain before the expiration date to avoid any disruptions to your website or email services.\n\nThank you for choosing us as your domain provider.\n\nSincerely,\nThe Domain Management Team'
            html_content = render_to_string('appone/renewal_alert_email.html', {'domain': domain})
            recipient_list = domain.notify.split(',')
            msg = EmailMultiAlternatives(subject, text_content, 'nandhini.veliiyangiri08@gmail.com', recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        # Send reminder 1 week before due date
        elif domain.due_date <= today + one_week and domain.due_date > today + one_day:
            subject = f'Renewal Alert: {domain.title} - 1 week reminder'
            text_content = f'Dear {domain.domain_account},\n\nThis is a reminder that your domain {domain.title} is due for renewal in 1 week, on {domain.due_date}.\n\nPlease ensure that you renew your domain before the expiration date to avoid any disruptions to your website or email services.\n\nThank you for choosing us as your domain provider.\n\nSincerely,\nThe Domain Management Team'
            html_content = render_to_string('appone/renewal_alert_email.html', {'domain': domain})
            recipient_list = domain.notify.split(',')
            msg = EmailMultiAlternatives(subject, text_content, 'nandhini.veliiyangiri08@gmail.com', recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        # Send reminder 1 day before due date
        elif domain.due_date <= today + one_day:
            subject = f'Renewal Alert: {domain.title} - 1 day reminder'
            text_content = f'Dear {domain.domain_account},\n\nThis is a reminder that your domain {domain.title} is due for renewal tomorrow, on {domain.due_date}.\n\nPlease ensure that you renew your domain before the expiration date to avoid any disruptions to your website or email services.\n\nThank you for choosing us as your domain provider.\n\nSincerely,\nThe Domain Management Team'
            html_content = render_to_string('appone/renewal_alert_email.html', {'domain': domain})
            recipient_list = domain.notify.split(',')
            msg = EmailMultiAlternatives(subject, text_content, 'nandhini.veliiyangiri08@gmail.com', recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()


def send_alerts(request):
    send_renewal_alerts()
    return HttpResponse('Renewal alerts sent successfully.')

@login_required
def create_domain(request):
    
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            domain = form.save()
            return redirect('domain_detail', pk=domain.pk)
    else:
        form = DomainForm()
    context = {'form': form}
    return render(request, 'appone/create_domain.html', context)

@login_required
def domain_detail(request, pk):
    domain = Domain.objects.get(pk=pk)
    return render(request, 'appone/domain_detail.html', {'domain': domain})

@login_required
def home(request):
    return render(request, 'base.html')

@never_cache
@login_required(login_url='login')
def dashboard(request):
    #domains and hosting count
    domains_count = Domain.objects.count()
    hosting_count = Hosting.objects.count()

    #renewal count
    domains_renewal =Domain.objects.filter(due_date__gte=timezone.now())
    domains_renewal_count =Domain.objects.filter(due_date__gte=timezone.now()).count()
    hosting_renewal = Hosting.objects.filter(renewal_date__gte=timezone.now())
    hosting_renewal_count =Hosting.objects.filter(renewal_date__gte=timezone.now()).count()

    #month and date dynamic
    current_month = datetime.now().strftime("%B").upper()
 # get current month name in all caps
    current_year = datetime.now().strftime("%Y") # get current year

    context = {'domains_count': domains_count, 'hosting_count': hosting_count, 'domains_renewal': domains_renewal , 'domains_renewal_count':domains_renewal_count , 'hosting_renewal':hosting_renewal ,'hosting_renewal_count':hosting_renewal_count , 'current_month':current_month ,'current_year':current_year  }
    return render(request, 'dashboard.html', context)

@login_required
def manage(request):
    domains = Domain.objects.all()
    
    return render(request, 'appone/manage.html', {'domains': domains })

def manage_copy(request):
    domains = Domain.objects.all()
    
    return render(request, 'appone/manage_copy.html', {'domains': domains })

@login_required
def upcoming_domains(request):
    domains = Domain.objects.filter(due_date__gte=timezone.now())
    return render(request, 'appone/upcoming_domains.html', {'domains': domains})


def edit_domain(request, domain_id):
    domain = get_object_or_404(Domain, id=domain_id)

    if request.method == 'POST':
        form = DomainForm(request.POST, instance=domain)
        if form.is_valid():
            form.save()
            return redirect(reverse('manage'))
    else:
        form = DomainForm(instance=domain)
        
    return render(request, 'appone/edit_domain.html', {'form': form})



def delete_domain(request, domain_id):
    domain = get_object_or_404(Domain, id=domain_id)
    if request.method == 'POST':
        domain.delete()
        return redirect('manage')
    else:
        return render(request, 'appone/delete_domain.html', {'domain': domain})
