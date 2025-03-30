from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponse
from django.views.decorators.http import require_GET

def home(request):
    form = ContactForm()
    return render(request, "core/home.html", {'form': form})

def privacy_view(request):
    template_name = "core/policy/privacy.html"
    return render(request, template_name)

def terms_view(request):
    template_name = "core/policy/terms.html"
    return render(request, template_name)

def cookie_view(request):
    template_name = "core/policy/cookies.html"
    return render(request, template_name)

def handler500(request):
    return render(request, 'error/500.html', status=500)

def handler403(request, exception):
    return render(request, 'error/403.html', status=403)

from news.models import Post, Category
from django.utils import timezone
from django.shortcuts import get_object_or_404

def handler404(request, exception):
    # Define which category to show (by slug)
    category_slug = "tech-va"  # Change this to your desired category slug
    
    try:
        # Try to get the category
        category = get_object_or_404(Category, slug=category_slug)
        
        # Get posts from the category
        category_posts = Post.objects.filter(
            category=category,
            status="published", 
            publish_date__lte=timezone.now()
        ).order_by('-publish_date')[:4]
        
    except:
        # Fallback to recent posts if category doesn't exist
        category_posts = Post.objects.filter(
            status="published", 
            publish_date__lte=timezone.now()
        ).order_by('-publish_date')[:3]
        category = None
    
    context = {
        'category_posts': category_posts,
        'selected_category': category
    }
    
    return render(request, 'error/404.html', context, status=404)

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Allow: /",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")