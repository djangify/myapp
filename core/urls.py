from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # cluster pages
    path(
        "tech-va/",
        TemplateView.as_view(template_name="core/tech-va.html"),
        name="tech_va",
    ),
    path(
        "ai-search-readiness/",
        TemplateView.as_view(template_name="core/ai-search-readiness.html"),
        name="ai_search",
    ),
    path(
        "local-business-ai-search/",
        TemplateView.as_view(template_name="core/local-business-ai-search.html"),
        name="local_ai_search",
    ),
    # policies
    path("policy/privacy/", views.privacy_view, name="privacy_policy"),
    path("policy/cookies/", views.cookie_view, name="cookie_policy"),
    path("policy/affiliate/", views.affiliate_view, name="affiliate_policy"),
    path("policy/terms/", views.terms_view, name="terms_conditions"),
    path("policy/support/", views.support_view, name="support_policy"),
    path("policy/", views.policies_index_view, name="policies_index"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
