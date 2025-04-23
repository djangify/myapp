from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import ContactSubmission
from .forms import ContactForm
import requests

def contact_view(request):
    form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        # Check for personal email domains before form validation
        email = request.POST.get('email', '')
        if email:
            domain = email.split('@')[-1].lower()
            # Check against the same list as in the form
            blocked_domains = [
                'gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com',
                'proton.me', 'protonmail.com', 'aol.com', 'icloud.com',
                'mail.com', 'zoho.com', 'yandex.com', 'gmx.com',
                'live.com', 'msn.com'
            ]
            
            if domain in blocked_domains:
                # Redirect to error page with email info
                return render(request, 'contact/email_error.html', {'email': email})
        
        # If email domain check passes, continue with normal form validation
        if form.is_valid():
            # Get cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data.get('phone', '')
            service_type = form.cleaned_data['service_type']
            used_before = form.cleaned_data['used_before']
            message = form.cleaned_data['message']
            
            # Get IP address and user agent
            ip_address = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            
            # Check if IP is blocked
            if ContactSubmission.objects.filter(ip_address=ip_address, is_blocked=True).exists():
                # Silently fail without letting the user know they're blocked
                return redirect('contact:thanks', submission_id=1)
            
            # Save to database with IP address
            submission = ContactSubmission.objects.create(
                name=name,
                email=email,
                phone=phone,
                service_type=service_type,
                used_before=used_before,
                message=message,
                ip_address=ip_address,
                user_agent=user_agent
            )
            
            # Send email notification
            try:
                # Email sending code here...
                pass
            except Exception as e:
                print(f"Email sending error: {str(e)}")
            
            # Redirect to thank you page with submission ID
            return redirect('contact:thanks', submission_id=submission.id)
        else:
            # If there are other form errors, show them
            messages.error(request, 'Please correct the errors in the form.')
    
    return render(request, 'contact/contact.html', {'form': form})

def thanks_view(request, submission_id):
    # Get the submission to display its details
    submission = get_object_or_404(ContactSubmission, id=submission_id)
    
    return render(request, 'contact/thanks.html', {
        'submission': submission
    })

def email_error_view(request):
    # This view is used if you want to access the error page directly
    return render(request, 'contact/email_error.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
