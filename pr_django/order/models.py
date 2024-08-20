# from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

from product.models import Product

class Order(models.Model):
    
    PENDING = 'pending'
    PROCESSING = 'processing'
    CANCELLED = 'cancelled'
    SHIPPED = 'shipped'
    ARRIVED = 'arrived'
    COMPLETED = 'completed'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (CANCELLED, 'Canceled'),
        (SHIPPED, 'Shipped'),
        (ARRIVED, 'Arrived'),
        (COMPLETED, 'Completed')
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=100, decimal_places=0, blank=True, null=True)
    stripe_token = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    status_updated_at = models.DateTimeField(auto_now=True)


    # items = OrderItemSerializer(many=True)
    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.first_name
    
    def get_order_items(self):
        return OrderItem.objects.filter(order=self)

class OrderItem(models.Model):
    # id=None
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=0)
    quantity = models.IntegerField(default=1)
    # print(id)

    def __str__(self):
        return '%s' % self.id