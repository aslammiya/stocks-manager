# Generated by Django 5.1.1 on 2024-09-06 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='ticker',
            new_name='ticker_symbol',
        ),
    ]
