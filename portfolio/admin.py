from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import Technology, Portfolio, PortfolioImage

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1
    fields = ('image', 'image_url', 'caption', 'order', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.display_image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.display_image)
        return "No image"

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "icon", "category")
    list_filter = ("category",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["name", "-created_at"]

class PortfolioAdminForm(forms.ModelForm):
    # No need to define widgets since we're using ProseEditorField
    class Meta:
        model = Portfolio
        fields = '__all__'

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioAdminForm
    list_display = (
        "title",
        "image_preview",
        "status",
        "is_featured",
        "order",
        "created_at",
    )
    list_filter = ("status", "is_featured", "technologies", "created_at")
    search_fields = ("title", "short_description", "introduction", "conclusion")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("technologies",)
    inlines = [PortfolioImageInline]
    list_editable = ("order", "is_featured", "status")
    ordering = ["order", "-created_at"]

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "title", 
                "slug", 
                "short_description", 
                "project_timeline",
                "status",
            ),
            "classes": ("wide", "extrapretty"),
        }),
        ("Project Overview", {
            "fields": (
                "introduction",
                "business_logic", 
                "target_audience",
            ),
            "classes": ("wide", "extrapretty"),
        }),
        ("Technical Details", {
            "fields": (
                "tech_stack_description", 
                "architecture_description",
                "technologies",
            ),
            "classes": ("wide", "extrapretty"),
        }),
        ("Development", {
            "fields": (
                "feature_description",
                "development_process",
                "challenges",
                "bugs_and_fixes",
            ),
            "classes": ("wide", "extrapretty"),
        }),
        ("Results & Reflection", {
            "fields": (
                "outcome",
                "lessons_learned", 
                "future_improvements",
                "conclusion",
            ),
            "classes": ("wide", "extrapretty"),
        }),
        ("Media", {
            "fields": (
                "featured_image", 
                "featured_image_url",
                "demo_video_url",
            ),
            "classes": ("wide", "extrapretty"),
        }),
        ("External Links", {
            "fields": (
                "github_url",
                "external_url",
                "live_site_url",
                "is_featured",
                "order",
            ),
            "classes": ("wide", "extrapretty"),
        }),
        ("SEO", {
            "fields": ("meta_title", "meta_description", "meta_keywords"),
            "classes": ("collapse", "wide", "extrapretty"),
        }),
    )

    def image_preview(self, obj):
        if obj.display_image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.display_image)
        return "No image"

    image_preview.short_description = "Preview"
    