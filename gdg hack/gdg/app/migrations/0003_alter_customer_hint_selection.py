# Generated by Django 5.1.4 on 2025-03-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_task_preference_alter_task_importance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='hint_selection',
            field=models.CharField(choices=[('pet', "What is your pet's name?"), ('school', "What was your first school's name?"), ('color', 'What is your favorite color?')], max_length=20),
        ),
    ]
