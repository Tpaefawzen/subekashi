# Generated by Django 4.1.1 on 2023-06-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subekashi", "0017_alter_song_posttime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song", name="posttime", field=models.DateTimeField(),
        ),
    ]