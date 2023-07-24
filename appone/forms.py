from django import forms
from .models import Domain
from django.core.validators import validate_email

class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ['source', 'title', 'registered_date', 'due_date', 'domain_provider', 'status', 'notify', 'domain_account']
        widgets = {
            'registered_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'domain_provider': forms.Select(choices=[('fastcomet', 'Fastcomet'), ('godaddy', 'Godaddy'), ('hostinger', 'Hostinger')]),
            'status': forms.Select(choices=[('active', 'Active'), ('expired', 'Expired'), ('cancelled', 'Cancelled')]),
            'notify': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter comma separated email addresses', 'rows': 2}),

        }

    def clean_notify(self):
      notify_emails = [email.strip() for email in self.cleaned_data['notify'].split(',')]
      for email in notify_emails:
        validate_email(email)
      return ','.join(notify_emails)





    
