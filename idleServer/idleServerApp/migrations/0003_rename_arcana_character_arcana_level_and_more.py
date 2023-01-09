# Generated by Django 4.1.4 on 2023-01-09 15:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idleServerApp', '0002_alter_appuser_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='arcana',
            new_name='arcana_level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='armoring',
            new_name='armoring_level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='cooking',
            new_name='cooking_level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='fishing',
            new_name='fishing_level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='harvesting',
            new_name='harvesting_level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='logging',
            new_name='logging_level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='mining',
            new_name='mining_level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='smelting',
            new_name='smelting_level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='weapons',
            new_name='weapons_level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='wood_working',
            new_name='wood_working_level',
        ),
        migrations.RemoveField(
            model_name='character',
            name='xp',
        ),
        migrations.AddField(
            model_name='character',
            name='aranca_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='character',
            name='combat_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='character',
            name='cooking_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='character',
            name='fishing_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='character',
            name='harvesting_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='character',
            name='logging_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='character',
            name='mining_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='character',
            name='smelting_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='character',
            name='weapons_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='character',
            name='wood_working_xp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)]),
        ),
    ]
