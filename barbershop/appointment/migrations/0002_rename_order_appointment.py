# Generated by Django 4.2.2 on 2023-10-24 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Appointment',
        ),
    ]
