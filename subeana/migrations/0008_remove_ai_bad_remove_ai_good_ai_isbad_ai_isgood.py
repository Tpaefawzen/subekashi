# Generated by Django 4.0 on 2022-11-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subeana', '0007_remove_ai_isgood_ai_bad_ai_good_alter_ai_lyrics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ai',
            name='bad',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='good',
        ),
        migrations.AddField(
            model_name='ai',
            name='isbad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ai',
            name='isgood',
            field=models.BooleanField(default=False),
        ),
    ]