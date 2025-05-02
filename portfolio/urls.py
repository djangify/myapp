# Path: portfolio/urls.py
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.PortfolioListView.as_view(), name='portfolio_list'),
    path('<slug:slug>/', views.PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('technology/<slug:technology_slug>/', 
         views.portfolio_by_technology, 
         name='portfolio_by_technology'),
]