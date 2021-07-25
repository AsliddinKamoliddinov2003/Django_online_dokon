from django.urls import path
from .views import *


urlpatterns=[

    path("add-cart/<int:product_id>/", add_to_cart, name="add-to-cart"),

]