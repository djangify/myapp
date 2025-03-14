from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, PortfolioSitemap, TechnologySitemap, NewsSitemap, NewsCategorySitemap
from django.conf.urls.static import static

sitemaps = {
    "static": StaticViewSitemap,
    "portfolio": PortfolioSitemap,
    "technology": TechnologySitemap,
    "blog": NewsSitemap,
    "category": NewsCategorySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('news/', include('news.urls')),
    path('shop/', include('shop.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'
handler403 = 'core.views.handler403'