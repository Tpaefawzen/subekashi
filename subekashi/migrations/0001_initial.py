# Generated by Django 4.0 on 2023-08-04 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics', models.CharField(default='', max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('genetype', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Singleton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=100)),
                ('value', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=500)),
                ('channel', models.CharField(default='', max_length=500)),
                ('url', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('lyrics', models.CharField(blank=True, default='', max_length=10000, null=True)),
                ('ruigo', models.CharField(blank=True, default='', max_length=50000, null=True)),
                ('imitate', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('imitated', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('posttime', models.DateTimeField(blank=True, null=True)),
                ('uploaddata', models.DateField(blank=True, null=True)),
                ('isoriginal', models.BooleanField(default=False)),
                ('isjoke', models.BooleanField(default=False)),
                ('isjapanese', models.BooleanField(default=True)),
                ('isdraft', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Genesong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('similar', models.CharField(default='', max_length=100)),
                ('ai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subekashi.ai')),
            ],
        ),
        migrations.CreateModel(
            name='Genecategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=100)),
                ('ai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subekashi.ai')),
            ],
        ),
    ]
