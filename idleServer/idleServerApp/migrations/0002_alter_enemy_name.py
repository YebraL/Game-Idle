# Generated by Django 4.1.4 on 2023-01-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idleServerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemy',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
