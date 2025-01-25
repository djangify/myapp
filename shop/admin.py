# shop/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser, Category, Product, Order, Download

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

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

# Register the custom user model
admin.site.register(CustomUser, CustomUserAdmin)