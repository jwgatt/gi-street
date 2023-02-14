from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=1)
    stripe_token = models.CharField(max_length=250)

    # """change ordering of objects in admin panel"""
    class Meta:
        ordering = ['-created_at',]

    # string representation of object to increase readability in backend """
    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    # string representation of id to increase readability in backend
    def __str__(self):
        return '%s' % self.id
