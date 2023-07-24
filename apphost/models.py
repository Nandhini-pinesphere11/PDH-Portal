
from django.db import models

class Hosting(models.Model):
    OWN = 'own'
    CLIENT = 'client'
    SOURCE_CHOICES = (
        (OWN, 'Own'),
        (CLIENT, 'Client'),
    )
    
    source = models.CharField(choices=SOURCE_CHOICES, max_length=6, default=OWN)
    title = models.CharField(max_length=255 , default=None)
    site = models.CharField(choices=[('static', 'Static'), ('dynamic', 'Dynamic'), ('ecommerce', 'Ecommerce')], max_length=255, default=None)
    purchased_date = models.DateField(default=None)
    renewal_date = models.DateField(default=None)
    website_hosting = models.CharField(choices=[('fastcomet', 'Fastcomet'), ('hostinger', 'Hostinger'), ('godaddy', 'Godaddy')], max_length=255, default=None)
    domain_purchased = models.CharField(choices=[('fastcomet', 'Fastcomet'), ('hostinger', 'Hostinger'), ('godaddy', 'Godaddy')], max_length=255 , default=None)
    dns_transferred_from = models.CharField(max_length=255 , default=None)
    hosting_account =models.CharField(max_length=255 , default=None)
    notify = models.CharField(max_length=255)

    def __str__(self):
        return self.title