from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import ContactSubmission
from .forms import ContactForm
import requests

def contact_view(request):
    recaptcha_public_key = settings.RECAPTCHA_PUBLIC_KEY
    form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        # Validate reCAPTCHA v3
        recaptcha_response = request.POST.get('g-recaptcha-response')
        if not recaptcha_response:
            messages.error(request, 'reCAPTCHA verification failed. Please try again or disable any browser extensions that might block reCAPTCHA.')
            return render(request, 'contact/contact.html', {'form': form, 'recaptcha_public_key': recaptcha_public_key})

        # Verify with Google
        recaptcha_secret = settings.RECAPTCHA_PRIVATE_KEY
        data = {
            'secret': recaptcha_secret,
            'response': recaptcha_response
        }

    try:
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        
        # With v3, check success and score
        if not result.get('success') or float(result.get('score', 0)) < 0.5:
            print(f"reCAPTCHA failed: {result}")  # Log the result for debugging
            messages.error(request, 'Our security check indicates you might be a bot. Please try again.')
            return render(request, 'contact/contact.html', {'form': form, 'recaptcha_public_key': recaptcha_public_key})
    except Exception as e:
        print(f"reCAPTCHA verification error: {str(e)}")
        # Continue anyway if there's a connection issue with Google
        
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
                # Email logic
                subject = f'New Contact Form Submission: {name}'
                
                # Get the service type display name
                service_display = dict(ContactSubmission.SERVICE_CHOICES).get(service_type, service_type)
                used_before_display = dict(ContactSubmission.USED_BEFORE_CHOICES).get(used_before, used_before)
                
                email_context = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'service_type': service_display,
                    'used_before': used_before_display,
                    'message': message,
                    'created_at': submission.created_at,
                    'ip_address': ip_address,
                    'user_agent': user_agent
                }
                
                # Render email templates
                email_html = render_to_string('contact/email/contact_notification.html', email_context)
                email_txt = render_to_string('contact/email/contact_notification.txt', email_context)
                
                # Send email
                send_mail(
                    subject=subject,
                    message=email_txt,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['djangify@gmail.com'],
                    html_message=email_html,
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending error: {str(e)}")
            
            # Redirect to thank you page with submission ID
            return redirect('contact:thanks', submission_id=submission.id)
        else:
            messages.error(request, 'Please correct the errors in the form.')
    
    return render(request, 'contact/contact.html', {'form': form, 'recaptcha_public_key': recaptcha_public_key})


def thanks_view(request, submission_id):
    # Get the submission to display its details
    submission = get_object_or_404(ContactSubmission, id=submission_id)
    
    return render(request, 'contact/thanks.html', {
        'submission': submission
    })

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
