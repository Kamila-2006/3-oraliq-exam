# Generated by Django 5.1.5 on 2025-01-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=2, unique=True),
            preserve_default=False,
        ),
    ]
