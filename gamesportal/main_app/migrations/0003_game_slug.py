# Generated by Django 5.0 on 2023-12-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_game_tags_gamelist_games_alter_tag_name_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]