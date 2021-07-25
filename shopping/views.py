from django.shortcuts import redirect, render
from store.models import Product
from django.urls import reverse
from .models import Cart,CartItem


def get_cart(request):
    session_id = request.session.session_key
    if session_id:
        session_id = request.session.create()

    cart = Cart.objects.filter(session_id=session_id)
    if cart.exists():
        cart = cart.first()
    else:
        cart = Cart(session_id=session_id).save()

    return cart
    



def add_to_cart(request,product_id):
    try:
        product = Product.objects.filter(id=product_id)
    except Product.DoesNotExist:
        return redirect(reverse("home-page"))

    cart = get_cart(request)
    cartitem = CartItem(product=product, cart=cart, price=product.price)
    cartitem.save()


    return render(request, "cart.html")
