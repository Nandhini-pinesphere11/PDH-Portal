# Generated by Django 4.1.7 on 2023-03-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0004_remove_hostingdetail_hosting_remove_domain_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain_account',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='domain',
            name='domain_provider',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='domain',
            name='notify',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='domain',
            name='status',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='domain',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
