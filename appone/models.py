from django.db import models

class Domain(models.Model):
    OWN = 'own'
    CLIENT = 'client'
    SOURCE_CHOICES = (
        (OWN, 'Own'),
        (CLIENT, 'Client'),
    )
    
    source = models.CharField(choices=SOURCE_CHOICES, max_length=6, default=OWN)
    title = models.CharField(max_length=255)
    registered_date = models.DateField()
    due_date = models.DateField()
    domain_provider = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    notify = models.CharField(max_length=255)
    domain_account = models.CharField(max_length=255)

    def __str__(self):
        return self.title

