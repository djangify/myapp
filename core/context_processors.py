# core/context_processors.py
from .models import HomePageSettings


def homepage_settings(request):
    try:
        settings = HomePageSettings.objects.first()
        social_links = []
        if settings:
            raw_links = [
                (settings.social_1_name, settings.social_1_url),
                (settings.social_2_name, settings.social_2_url),
            ]
            social_links = [(n, u) for n, u in raw_links if n and u]
    except Exception:
        settings = None
        social_links = []
    return {
        "homepage_settings": settings,
        "social_links": social_links,  # ✅ available everywhere
    }
