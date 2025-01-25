from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils import timezone
import stripe
from .models import Product, Order, Download
import os

stripe.api_key = settings.STRIPE_SECRET_KEY

def product_list(request):
    products = Product.objects.filter(status='published').order_by('-created_at')
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, status='published')
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def checkout(request, slug):
    product = get_object_or_404(Product, slug=slug, status='published')
    
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(product.price * 100),  # Convert to cents
            currency='usd',
            metadata={'product_id': product.id}
        )
        return render(request, 'shop/checkout.html', {
            'product': product,
            'client_secret': intent.client_secret,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
    except Exception as e:
        messages.error(request, "Unable to initialize checkout.")
        return redirect('shop:product_detail', slug=slug)

@login_required
def payment_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/payment_success.html', {'order': order})

@login_required
def user_dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/dashboard.html', {'orders': orders})

@login_required
def download_product(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if order.status != 'completed':
        raise Http404("Order not completed")
    
    download, created = Download.objects.get_or_create(order=order)
    
    if not os.path.exists(order.product.digital_file.path):
        raise Http404("File not found")
    
    download.download_count += 1
    download.last_downloaded = timezone.now()
    download.save()
    
    response = HttpResponse(order.product.digital_file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(order.product.digital_file.name)}"'
    return response

@login_required
def webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        
        # Create order
        try:
            product_id = payment_intent.metadata.get('product_id')
            product = Product.objects.get(id=product_id)
            
            Order.objects.create(
                user=request.user,
                product=product,
                amount=product.price,
                status='completed',
                stripe_payment_intent=payment_intent.id,
                stripe_payment_status='succeeded'
            )
        except Exception as e:
            return HttpResponse(status=400)

    return HttpResponse(status=200)