# Generated by Django 4.0 on 2022-12-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subekashi', '0005_alter_song_imitated'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='isoriginal',
            field=models.BooleanField(default=False),
        ),
    ]
