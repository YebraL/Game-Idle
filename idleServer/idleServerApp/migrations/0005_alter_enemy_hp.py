# Generated by Django 4.1.4 on 2023-01-09 15:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idleServerApp', '0004_enemy_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemy',
            name='hp',
            field=models.IntegerField(default=50, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)]),
        ),
    ]
