# Path: portfolio/models.py
from django.db import models
from django.core.validators import FileExtensionValidator
from django_prose_editor.fields import ProseEditorField

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
    icon = models.CharField(max_length=50, blank=True, null=True)
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
    short_description = ProseEditorField(max_length=200)
    project_timeline = models.CharField(max_length=100, blank=True, help_text="When the project was built, e.g., 'Jan-Mar 2023'")
    
    # Content sections
    introduction = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Introduction section describing the project overview"
    )
    business_logic = ProseEditorField(
        blank=True, 
        null=True,
        help_text="The problem statement and business logic of the project"
    )
    target_audience = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Description of who the project is designed for"
    )
    tech_stack_description = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Detailed description of the technical stack and architecture"
    )
    architecture_description = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Explanation of architecture and design patterns used"
    )
    feature_description = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Description of key features and functionality"
    )
    development_process = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Approach and methodologies used during development"
    )
    challenges = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Technical hurdles faced and how they were overcome"
    )
    bugs_and_fixes = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Significant issues encountered and their resolutions"
    )
    outcome = ProseEditorField(
        blank=True, 
        null=True,
        help_text="How the project meets its objectives"
    )
    lessons_learned = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Technical and project management insights gained"
    )
    future_improvements = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Planned or potential future enhancements"
    )
    conclusion = ProseEditorField(
        blank=True, 
        null=True,
        help_text="Summary of the project experience"
    )

# Media
    featured_image = models.ImageField(
        upload_to='portfolio/featured/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
        blank=True,
        null=True
    )
    featured_image_url = models.URLField(blank=True, null=True)
    demo_video_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to a demo video (e.g., YouTube)"
    )
    technologies = models.ManyToManyField(Technology, related_name="portfolios")
    
    # External links
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
    
    # Status and ordering
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    
    # Timestamps and SEO
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
