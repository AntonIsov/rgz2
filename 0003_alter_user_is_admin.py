# Generated by Django 5.1.2 on 2024-12-05 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
