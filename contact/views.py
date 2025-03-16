from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import ContactSubmission

def contact_view(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        service_type = request.POST.get('service_type', '')
        used_before = request.POST.get('used_before', '')
        message = request.POST.get('message', '')
        
        # Validate required fields
        if not all([name, email, service_type, used_before, message]):
            messages.error(request, 'Please fill in all required fields.')
            return redirect('contact:contact')
        
        # Save to database
        submission = ContactSubmission.objects.create(
            name=name,
            email=email,
            phone=phone,
            service_type=service_type,
            used_before=used_before,
            message=message
        )
        
        # Send email notification
        try:
            # Prepare email content
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
            # Log the error but don't show technical details to user
            print(f"Email sending error: {str(e)}")
        
        # Redirect to thank you page with submission ID
        return redirect('contact:thanks', submission_id=submission.id)
    
    return render(request, 'contact/contact.html')

def thanks_view(request, submission_id):
    # Get the submission to display its details
    submission = get_object_or_404(ContactSubmission, id=submission_id)
    
    return render(request, 'contact/thanks.html', {
        'submission': submission
    })