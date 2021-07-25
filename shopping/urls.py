from django.urls import path
from .views import *


urlpatterns=[

    path("add-cart-item/<int:product_id>/", add_cart_item, name="add-cart-item"),
    path("subtract-cart-item/<int:product_id>/",subtract_cart_item, name="subtract-cart-item"),
    path("remove-cart-item/<int:product_id>/",remove_cart_item, name="remove-cart-item"),
    path("cart/", cart, name="cart"),

]