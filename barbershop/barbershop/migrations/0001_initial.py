# Generated by Django 4.2.2 on 2023-10-24 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barber_name', models.CharField(max_length=100)),
                ('barber_image', models.ImageField(upload_to='barbers/images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]