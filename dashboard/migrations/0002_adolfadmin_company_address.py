# Generated by Django 4.1.2 on 2023-02-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adolfadmin',
            name='company_address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
