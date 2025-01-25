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

def handler404(request, exception):
    return render(request, 'error/404.html', status=404)

def handler500(request):
    return render(request, 'error/500.html', status=500)

def handler403(request, exception):
    return render(request, 'error/403.html', status=403)