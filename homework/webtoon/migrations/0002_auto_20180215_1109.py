# Generated by Django 2.0.2 on 2018-02-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtoon',
            name='img_url',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='webtoon',
            name='week_webtoon',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]