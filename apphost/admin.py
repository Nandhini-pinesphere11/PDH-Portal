from django.contrib import admin
from .models import Hosting
from .forms import HostingForm

@admin.register(Hosting)
class HostingAdmin(admin.ModelAdmin):
    form = HostingForm