from django.contrib import admin

from .models import Cart, CartItem, Cupon, CuponGroup



class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "session_id"]

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
admin.site.register(Cupon)
admin.site.register(CuponGroup)