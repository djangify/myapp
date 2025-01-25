from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include
from django.views.static import serve 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('news/', include('news.urls')),
    path('media/<path:path>', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'
handler403 = 'core.views.handler403'