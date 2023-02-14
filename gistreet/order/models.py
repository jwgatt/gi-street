from django.contrib.auth.models import User
from django.db import models
from product.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE, )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    created_at = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True)
    paid_amount = models.DecimalField(
        max_digits=8, decimal_places=2, default=1)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
