from django.shortcuts import render, redirect, get_object_or_404
from .forms import HostingForm
from .models import Hosting
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def create_hosting(request):
    
    if request.method == 'POST':
        form = HostingForm(request.POST)
        if form.is_valid():
            hosting = form.save()
            return redirect('hosting_detail', pk=hosting.pk)
    else:
        form = HostingForm()
    context = {'form': form}
    return render(request, 'apphost/create_hosting.html', context)

@login_required
def hosting_detail(request, pk):
    hosting = Hosting.objects.get(pk=pk)
    return render(request, 'apphost/hosting_detail.html', {'hosting': hosting})


def edit_hosting(request, host_id):
    host = get_object_or_404(Hosting, id=host_id)
    if request.method == 'POST':
        form = HostingForm(request.POST, instance=host)
        if form.is_valid():
            form.save()
            return redirect(reverse('manage-host'))
    else:
        form = HostingForm(instance=host)
    return render(request, 'apphost/edit_hosting.html', {'form': form})


def delete_hosting(request, host_id):
    host = get_object_or_404(Hosting, id=host_id)
    if request.method == 'POST':
        host.delete()
        return redirect('manage-host')
    else:
        return render(request, 'apphost/delete_hosting.html', {'host': host})


@login_required
def manage_host(request):
    hosting = Hosting.objects.all()
    return render(request, 'apphost/manage_host.html', {'hosting': hosting})

@login_required
def upcoming_hosting(request):
    hosting = Hosting.objects.filter(renewal_date__gte=timezone.now())
    return render(request, 'apphost/upcoming_hosting.html', {'hosting': hosting })





    