# Generated by Django 5.1.2 on 2024-12-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0007_task_is_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='who_create',
            field=models.CharField(default='', max_length=200),
        ),
    ]
