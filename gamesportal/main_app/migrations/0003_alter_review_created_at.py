# Generated by Django 5.0 on 2023-12-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_gamelist_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
