# Generated by Django 5.0.7 on 2024-08-03 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Изображение'),
        ),
    ]