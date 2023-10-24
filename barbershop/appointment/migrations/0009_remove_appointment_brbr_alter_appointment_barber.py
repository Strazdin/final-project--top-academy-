# Generated by Django 4.2.2 on 2023-10-24 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0004_alter_barbers_options_alter_price_options_and_more'),
        ('appointment', '0008_alter_appointment_options_alter_appointment_barber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='brbr',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='barber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='barbershop.barbers', verbose_name='Барбер'),
        ),
    ]