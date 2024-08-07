# Generated by Django 5.0.7 on 2024-08-07 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('KR', 'кыргыз тили'), ('RU', 'Русский язык')], default='RU', max_length=255, null=True, verbose_name='Язык')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Спецпроекты ',
                'verbose_name_plural': 'Спецпроекты ',
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Special.news')),
            ],
            options={
                'verbose_name': 'Изображение Спецпроекты ',
                'verbose_name_plural': 'Изображения Спецпроекты',
            },
        ),
    ]
