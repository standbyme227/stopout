# Generated by Django 2.0.2 on 2018-02-15 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_id', models.CharField(max_length=100)),
                ('episode_title', models.CharField(max_length=100)),
                ('episode_img_url', models.CharField(max_length=100)),
                ('episode_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Webtoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webtoon_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('week_webtoon', models.CharField(max_length=100)),
                ('img_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='webtoon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webtoon.Webtoon'),
        ),
    ]
