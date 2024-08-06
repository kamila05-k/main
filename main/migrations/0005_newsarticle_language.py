# Generated by Django 5.0.7 on 2024-08-05 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_newsarticle_image_newsarticleimage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='language',
            field=models.CharField(blank=True, choices=[('КР', 'кыргыз тили'), ('RU', 'Русский язык')], default='КР', max_length=255, null=True, verbose_name='Язык'),
        ),
    ]