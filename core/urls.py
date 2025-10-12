from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "digital-marketing-specialist",
        TemplateView.as_view(template_name="core/digital-marketing-specialist.html"),
        name="digital_marketing_specialist",
    ),
    path(
        "tech-va/",
        TemplateView.as_view(template_name="core/tech-va.html"),
        name="tech_va",
    ),
    path(
        "pdf-creation",
        TemplateView.as_view(template_name="core/pdf-creation.html"),
        name="pdf_creation",
    ),
    path("support/", views.support, name="support"),
    # policies
    path("policy/privacy/", views.privacy_view, name="privacy_policy"),
    path("policy/cookies/", views.cookie_view, name="cookie_policy"),
    path("policy/affiliate/", views.affiliate_view, name="affiliate_policy"),
    path("policy/ai-writing/", views.ai_writing_view, name="ai_writing_policy"),
    path("policy/terms/", views.terms_view, name="terms_conditions"),
    path("policy/support/", views.support_view, name="support_policy"),
    path("policy/", views.policies_index_view, name="policies_index"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
