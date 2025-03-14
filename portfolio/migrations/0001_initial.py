# Generated by Django 4.2.18 on 2025-03-13 19:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('short_description', models.CharField(max_length=200)),
                ('introduction', models.TextField(blank=True, help_text='Introduction section describing the project overview', null=True)),
                ('tech_stack_description', models.TextField(blank=True, help_text='Detailed description of the technical stack and architecture', null=True)),
                ('feature_description', models.TextField(blank=True, help_text='Description of key features and functionality', null=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='portfolio/featured/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])])),
                ('featured_image_url', models.URLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, help_text='URL to the GitHub repository for this project', null=True)),
                ('external_url', models.URLField(blank=True, help_text='URL to the external marketplace listing', null=True)),
                ('live_site_url', models.URLField(blank=True, help_text='URL to the live deployed project', null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default='draft', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('meta_title', models.CharField(blank=True, max_length=60)),
                ('meta_description', models.CharField(blank=True, max_length=160)),
                ('meta_keywords', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Portfolios',
                'ordering': ['order', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('icon', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('frontend', 'Frontend'), ('backend', 'Backend'), ('database', 'Database'), ('devops', 'DevOps'), ('mobile', 'Mobile'), ('other', 'Other')], default='other', help_text='Category of the technology', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Technologies',
                'ordering': ['name', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio/gallery/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.portfolio')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='technologies',
            field=models.ManyToManyField(related_name='portfolios', to='portfolio.technology'),
        ),
    ]
