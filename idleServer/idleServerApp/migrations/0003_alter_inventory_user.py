# Generated by Django 4.1.3 on 2023-01-07 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idleServerApp', '0002_alter_inventory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='character_inventory', to='idleServerApp.character'),
        ),
    ]
