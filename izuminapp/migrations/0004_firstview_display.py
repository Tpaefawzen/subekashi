# Generated by Django 4.0.2 on 2022-02-24 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izuminapp', '0003_firstview_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstview',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]
