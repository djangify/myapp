# Path: portfolio/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Technology, Portfolio, PortfolioImage

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'
    context_object_name = 'portfolios'
    queryset = Portfolio.objects.filter(status='published').order_by('order', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['technologies'] = Technology.objects.all()
        return context

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolio'
    
    def get_queryset(self):
        return Portfolio.objects.filter(status='published')

def portfolio_by_technology(request, technology_slug):
    technology = get_object_or_404(Technology, slug=technology_slug)
    portfolios = Portfolio.objects.filter(
        technologies=technology,
        status='published'
    ).order_by('order', '-created_at')
    
    return render(request, 'portfolio/portfolio_by_technology.html', {
        'technology': technology,
        'portfolios': portfolios
    })