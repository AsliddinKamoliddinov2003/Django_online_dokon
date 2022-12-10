from django.db import models

from store.models import *
from accounts.models import User



class ClientProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to="images/", null=True)
    phone_number = models.CharField(max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    appertment = models.PositiveIntegerField()
    pochta_code = models.CharField(max_length=25, null=True)
    status = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.client.first_name


class Order(models.Model):
    STATUS = [
        ("new", "New"),
        ("accepted", "Accepted"),
        ("completed", "Completed"),
        ("canceled", "Canceled")
    ]

    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="orders")
    order_number = models.CharField(max_length=20)
    status = models.CharField(max_length=50, choices=STATUS, default="new")
    ip = models.CharField(max_length=255, blank=True, null=True)
    is_ordered = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
     
    # def __str__(self):
    #     return self.client.first_name


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    reduced_price_order = models.FloatField(blank=True, default=0.0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    def total_price_order(self):
        if self.reduced_price_order != 0.0:
            return self.reduced_price_order * self.quantity
        else:
            return self.product.price * self.quantity