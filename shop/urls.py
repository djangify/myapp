# Path: shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('checkout/<slug:slug>/', views.checkout, name='checkout'),
    path('payment-success/<int:order_id>/', views.payment_success, name='payment_success'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('download/<int:order_id>/', views.download_product, name='download_product'),
    path('webhook/', views.webhook, name='webhook'),
]