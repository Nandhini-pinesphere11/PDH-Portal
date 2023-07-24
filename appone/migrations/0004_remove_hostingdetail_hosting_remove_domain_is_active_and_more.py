# Generated by Django 4.1.7 on 2023-03-24 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0003_alter_hosting_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostingdetail',
            name='hosting',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='name',
        ),
        migrations.AddField(
            model_name='domain',
            name='domain_account',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='domain',
            name='domain_provider',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='domain',
            name='due_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='domain',
            name='notify',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='domain',
            name='registered_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='domain',
            name='source',
            field=models.CharField(choices=[('own', 'Own'), ('client', 'Client')], default='own', max_length=6),
        ),
        migrations.AddField(
            model_name='domain',
            name='status',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='domain',
            name='title',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.DeleteModel(
            name='DomainDetail',
        ),
        migrations.DeleteModel(
            name='Hosting',
        ),
        migrations.DeleteModel(
            name='HostingDetail',
        ),
    ]
