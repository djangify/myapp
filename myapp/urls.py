from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from .sitemaps import (
    StaticViewSitemap,
    PortfolioSitemap,
    TechnologySitemap,
    NewsSitemap,
    NewsCategorySitemap,
)

sitemaps = {
    "static": StaticViewSitemap,
    "portfolio": PortfolioSitemap,
    "technology": TechnologySitemap,
    "blog": NewsSitemap,
    "category": NewsCategorySitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("news/", include("news.urls")),
    path("shop/", include("shop.urls")),
    path("contact/", include("contact.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("tinymce/", include("tinymce.urls")),
]

handler404 = "core.views.handler404"
handler500 = "core.views.handler500"
handler403 = "core.views.handler403"
