from django.contrib import admin
from .models import Domain
from .forms import DomainForm

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    form = DomainForm
