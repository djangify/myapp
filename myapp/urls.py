from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("news/", include("news.urls", namespace="news")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
