from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from portfolio.models import Portfolio, Technology
from news.models import Post, Category
from django.utils import timezone

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['core:home', 'core:privacy_policy', 'core:cookie_policy', 'core:terms_conditions', 
                'portfolio:portfolio_list', 'news:list']

    def location(self, item):
        url = reverse(item)
        # Remove any protocol prefix if it exists to prevent duplication
        if url.startswith('http'):
            url_parts = url.split('://', 1)
            if len(url_parts) > 1:
                return url_parts[1]
        return url

class PortfolioSitemap(Sitemap):
    priority = 1.0  # Highest priority as requested
    changefreq = 'weekly'

    def items(self):
        return Portfolio.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('portfolio:portfolio_detail', kwargs={'slug': obj.slug})

class TechnologySitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return Technology.objects.all()

    def location(self, obj):
        return reverse('portfolio:portfolio_by_technology', kwargs={'technology_slug': obj.slug})

class NewsSitemap(Sitemap):
    priority = 0.7
    changefreq = 'daily'

    def items(self):
        return Post.objects.filter(status='published', publish_date__lte=timezone.now())

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return reverse('news:detail', kwargs={'slug': obj.slug})

class NewsCategorySitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('news:category', kwargs={'slug': obj.slug})

# Combine all sitemaps in a dictionary
sitemaps = {
    'static': StaticViewSitemap,
    'portfolio': PortfolioSitemap,
    'technology': TechnologySitemap,
    'news': NewsSitemap,
    'news_category': NewsCategorySitemap,
}
