# Generated by Django 4.2.2 on 2023-11-04 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barber_name', models.CharField(db_index=True, max_length=20, verbose_name='Имя')),
                ('barber_image', models.ImageField(upload_to='barbers/images/')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Был добавлен')),
            ],
            options={
                'verbose_name': 'Барбера',
                'verbose_name_plural': 'Барберы',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(db_index=True, max_length=100, verbose_name='Название услуги')),
                ('price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Стрижка',
                'verbose_name_plural': 'Прайс-лист',
                'ordering': ['-price'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_small', models.ImageField(blank=True, null=True, upload_to='portfolio/images/', verbose_name='Фото маленькое')),
                ('image_big', models.ImageField(blank=True, null=True, upload_to='portfolio/images/', verbose_name='Фото большое')),
                ('end_photo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название большого фото')),
                ('barber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='barbershop.barbers', verbose_name='Барбер')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
            },
        ),
    ]
