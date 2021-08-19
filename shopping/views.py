from django.shortcuts import redirect, render
from store.models import Product
from django.urls import reverse
from .models import CartItem, Cupon
from .utils import get_cart, get_current_utc, delete_cart


def add_cart_item(request,cartitem_id):
    try:
        cartitem = CartItem.objects.get(id=cartitem_id)
        cartitem.quantity += 1    
        cartitem.save()
    except CartItem.DoesNotExist:
        pass
   
    return redirect(reverse("cart"))


def subtract_cart_item(request,cartitem_id):
    try:
        cartitem = CartItem.objects.get(id=cartitem_id)

        if cartitem.quantity == 1:
            cartitem.delete()
            cart = get_cart(request)
            delete_cart(cart)
        else:
            cartitem.quantity -= 1
            cartitem.save()
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
    context = {}

    cart = get_cart(request)
    cartitems = CartItem.objects.filter(cart=cart)
    
    if request.method=="POST":
        cupon_code = request.POST.get("cupon-code", None)
        if cupon_code:
            cupons = Cupon.objects.filter(code=cupon_code)
            if not cupons.exists():
                context["cupon_message"] = "The cupon code doesn't exist"
            else:
                cupon = cupons.first()
                if  get_current_utc() > cupon.expires_in:
                    context["cupon_message"] = "The cupon code expired"
                else:
                    for cartitem in cartitems:
                        categories = []
                        for category in cupon.category.all():
                            categories.append(category.name)
                        category = cartitem.product.sub_category.name
                        if category in categories:
                            if cartitem.reduced_price:
                                cartitem.reduced_price = (cartitem.reduced_price*(100 - cupon.stock))/100
                            else:
                                cartitem.reduced_price = (cartitem.product.price*(100 - cupon.stock))/100
                            cupon.is_used=True
                            cartitem.save()

    context["cartitems"] = cartitems
    return render(request, "cart.html",context)
                    

        
        


