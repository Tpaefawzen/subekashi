# Generated by Django 4.0 on 2022-11-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subeana', '0004_song_ruigo_delete_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='lyrics',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='ruigo',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
    ]