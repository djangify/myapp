# Path: portfolio/models.py
from django.db import models
from django.core.validators import FileExtensionValidator

class Technology(models.Model):
    TECH_CATEGORIES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('mobile', 'Mobile'),
        ('other', 'Other')
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50)
    category = models.CharField(
        max_length=20,
        choices=TECH_CATEGORIES,
        default='other',
        help_text="Category of the technology"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name', '-created_at']

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived')
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=200)
    
    # Content sections
    introduction = models.TextField(
        blank=True, 
        null=True,
        help_text="Introduction section describing the project overview"
    )
    tech_stack_description = models.TextField(
        blank=True, 
        null=True,
        help_text="Detailed description of the technical stack and architecture"
    )
    feature_description = models.TextField(
        blank=True, 
        null=True,
        help_text="Description of key features and functionality"
    )

    featured_image = models.ImageField(
        upload_to='portfolio/featured/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
        blank=True,
        null=True
    )
    featured_image_url = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField(Technology, related_name="portfolios")
    github_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to the GitHub repository for this project",
    )
    external_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to the external marketplace listing",
    )
    live_site_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to the live deployed project",
    )
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name_plural = "Portfolios"

    def __str__(self):
        return self.title

    @property
    def display_image(self):
        return self.featured_image_url or (self.featured_image.url if self.featured_image else None)


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='portfolio/gallery/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
        blank=True,
        null=True
    )
    image_url = models.URLField(blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.portfolio.title} - Image {self.order}"

    @property
    def display_image(self):
        return self.image_url or (self.image.url if self.image else None)