from django.db.models.fields import NOT_PROVIDED
from django.shortcuts import redirect, render
from store.models import Product
from django.urls import reverse
from .models import CartItem, Cupon
from .utils import get_cart



def add_cart_item(request,cartitem_id):
    try:
        cartitem = CartItem.objects.get(id=cartitem_id)
        cartitem.quantity += 1    
    except CartItem.DoesNotExist:
        pass
    cartitem.save()
   
    return redirect(reverse("cart"))


def subtract_cart_item(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect(reverse("home-page"))

    cart = get_cart(request)
    try:
        cartitem = CartItem.objects.get(cart=cart, product=product)
        if cartitem.quantity > 1:
            cartitem.quantity -= 1    
            cartitem.save()
        else:
            cartitem.delete()
    except CartItem.DoesNotExist:
        pass

   
    return redirect(reverse("cart"))


def remove_cart_item(request, cartitem_id):
    try:
        cartitem = CartItem.objects.get(id = int(cartitem_id))
        cartitem.delete()
    except CartItem.DoesNotExist:
        pass

   
    return redirect(reverse("cart"))



def cart(request):
    cart = get_cart(request)
    cartitems = CartItem.objects.filter(cart=cart)
    context = {
        "cartitems":cartitems
    }
    return render(request, "cart.html",context)


# def apply(request, code):
#     code = request.POST.get('code', None)
#     cupon = Cupon.objects.all()
#     if cupon.code == code and cupon.is_used==True:

