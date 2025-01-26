# shop/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Order, Download

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'status', 'created_at', 'display_thumbnail')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('title', 'description', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('display_image_preview',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'status')
        }),
        ('Product Details', {
            'fields': ('short_description', 'description', 'price')
        }),
        ('Digital Product', {
            'fields': ('digital_file',),
        }),
        ('Product Image', {
            'fields': ('image', 'external_image_url', 'display_image_preview'),
        }),
    )

    def display_thumbnail(self, obj):
        if obj.display_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.display_image)
        return "-"
    display_thumbnail.short_description = 'Thumbnail'

    def display_image_preview(self, obj):
        if obj.display_image:
            return format_html('<img src="{}" width="300" style="max-height: 300px; object-fit: contain;" />', obj.display_image)
        return "-"
    display_image_preview.short_description = 'Image Preview'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('reference', 'user', 'product', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('reference', 'user__email', 'product__title')
    readonly_fields = ('reference', 'stripe_payment_intent', 'stripe_payment_status')
    
    fieldsets = (
        (None, {
            'fields': ('reference', 'user', 'product', 'amount', 'status')
        }),
        ('Payment Information', {
            'fields': ('stripe_payment_intent', 'stripe_payment_status'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ('order', 'download_count', 'last_downloaded', 'created_at')
    list_filter = ('created_at', 'last_downloaded')
    search_fields = ('order__reference', 'order__user__email')
    readonly_fields = ('download_count', 'last_downloaded')