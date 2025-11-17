from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from django.utils import timezone
from datetime import timedelta

@shared_task
def send_order_confirmation_email(order_id):
    try:
        order = Order.objects.get(id=order_id)
        send_mail(
            subject=f"Order Confirmation #{order.id}",
            message=f"Dear {order.user.username}, your order has been received!",
            from_email='no-reply@furnitureshop.com',
            recipient_list=[order.user.email],
        )
    except Order.DoesNotExist:
        pass

@shared_task
def update_order_status(order_id=None):
    if order_id:
        try:
            order = Order.objects.get(id=order_id)
            if order.status.lower() == 'pending':
                order.status = 'processing'
                order.save()
        except Order.DoesNotExist:
            pass
    else:
        pending_orders = Order.objects.filter(
            status__iexact='pending',
            created_at__lte=timezone.now() - timedelta(minutes=5)
        )
        for order in pending_orders:
            order.status = 'processing'
            order.save()

@shared_task
def update_order_status():

    pending_orders = Order.objects.filter(status='Pending', created_at__lte=timezone.now() - timedelta(minutes=5))
    for order in pending_orders:
        order.status = 'Processing'
        order.save()
