# Generated by Django 4.2.11 on 2024-04-22 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_cooking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='is_healthy',
        ),
    ]
