from django import forms
from .models import Hosting

class HostingForm(forms.ModelForm):
    class Meta:
        model = Hosting
        fields = ['source', 'title', 'site', 'purchased_date', 'renewal_date', 'website_hosting', 'domain_purchased', 'dns_transferred_from', 'hosting_account', 'notify']
        widgets = {
            'source': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'site':forms.Select(attrs={'class': 'form-control'}),
            'purchased_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'renewal_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'website_hosting': forms.Select(attrs={'class': 'form-control'}),
            'domain_purchased': forms.Select(attrs={'class': 'form-control'}),
            'dns_transferred_from': forms.TextInput(attrs={'class': 'form-control'}),
            'hosting_account': forms.TextInput(attrs={'class': 'form-control'}),
            'notify': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter comma separated email addresses', 'rows': 2}),
        }
