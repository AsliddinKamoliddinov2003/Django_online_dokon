from store.models import Product
from django.db import models
from django.contrib.auth import get_user_model

Client = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

class Cart_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    