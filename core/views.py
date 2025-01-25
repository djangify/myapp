from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")


def privacy_view(request):
    template_name = "core/policy/privacy.html"
    return render(request, template_name)


def terms_view(request):
    template_name = "core/policy/terms.html"
    return render(request, template_name)


def cookie_view(request):
    template_name = "core/policy/cookies.html"
    return render(request, template_name)
