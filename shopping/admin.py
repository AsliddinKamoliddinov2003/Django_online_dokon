from django.contrib import admin

from .models import Cart, CartItem, Cupon, CuponGroup

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Cupon)
admin.site.register(CuponGroup)