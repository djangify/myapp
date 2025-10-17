from django.views.generic import ListView, DetailView
from .models import InfoPage


class PolicyListView(ListView):
    model = InfoPage
    template_name = "infopages/policy_index.html"
    context_object_name = "pages"

    def get_queryset(self):
        return InfoPage.objects.filter(page_type="policy", published=True)


class DocListView(ListView):
    model = InfoPage
    template_name = "infopages/docs_index.html"
    context_object_name = "pages"

    def get_queryset(self):
        return InfoPage.objects.filter(page_type="doc", published=True)


class InfoPageDetailView(DetailView):
    model = InfoPage
    template_name = "infopages/detail.html"
    context_object_name = "page"
