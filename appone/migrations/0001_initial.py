# Generated by Django 4.1.7 on 2023-03-19 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('purchase_date', models.DateField()),
                ('renewal_date', models.DateField()),
                ('renewal_alerts', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosting_name', models.CharField(max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('purchase_date', models.DateField()),
                ('renewal_date', models.DateField()),
                ('renewal_alerts', models.PositiveIntegerField()),
            ],
        ),
    ]
