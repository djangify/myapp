from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
import stripe
import json
from .models import Order

@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        
        try:
            order = Order.objects.get(stripe_payment_intent=payment_intent.id)
            order.status = 'completed'
            order.stripe_payment_status = payment_intent.status
            order.save()
            
            # Create download record if not exists
            order.download_set.get_or_create()
            
        except Order.DoesNotExist:
            return HttpResponse(status=404)
            
    elif event.type == 'payment_intent.payment_failed':
        payment_intent = event.data.object
        
        try:
            order = Order.objects.get(stripe_payment_intent=payment_intent.id)
            order.status = 'failed'
            order.stripe_payment_status = payment_intent.status
            order.save()
        except Order.DoesNotExist:
            return HttpResponse(status=404)

    return HttpResponse(status=200)
