# Generated by Django 4.2.2 on 2023-11-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0002_tag_barbers_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbers',
            name='tags',
            field=models.ManyToManyField(blank=True, to='barbershop.tag'),
        ),
    ]