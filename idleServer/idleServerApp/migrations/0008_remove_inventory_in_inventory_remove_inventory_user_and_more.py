# Generated by Django 4.1.4 on 2023-01-04 20:19

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idleServerApp', '0007_character_enemy_item_armor_weapon_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='in_inventory',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='user',
        ),
        migrations.AddField(
            model_name='character',
            name='userInventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='character_inventory', to='idleServerApp.inventory'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='armor_inventory',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='inventory',
            name='item_inventory',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='inventory',
            name='weapon_inventory',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='max_spaces',
            field=models.PositiveIntegerField(),
        ),
    ]