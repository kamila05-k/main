# Generated by Django 5.0.7 on 2024-08-03 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_newsarticleimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='image',
        ),
        migrations.AddField(
            model_name='newsarticleimage',
            name='title',
            field=models.CharField(default=1, max_length=200, verbose_name='Заголовок'),
            preserve_default=False,
        ),
    ]