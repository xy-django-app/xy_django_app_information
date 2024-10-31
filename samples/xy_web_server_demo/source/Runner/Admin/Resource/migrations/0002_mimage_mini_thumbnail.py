# Generated by Django 5.1.2 on 2024-10-31 02:46

import Resource.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Resource", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mimage",
            name="mini_thumbnail",
            field=models.ImageField(
                blank=True,
                default=None,
                help_text="迷你缩略图",
                null=True,
                upload_to=Resource.models.mini__thumbnail,
                verbose_name="迷你缩略图",
            ),
        ),
    ]
