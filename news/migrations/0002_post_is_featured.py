# Generated by Django 5.1 on 2025-03-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False, help_text='Show this post at the top of the listing'),
        ),
    ]
