import json
from django.http.response import  JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required


from store.models import Product, ProductColor, ProductSize
from .models import CartItem, Cupon, Wishlist
from .utils import get_cart, get_current_utc, delete_cart


@login_required(login_url="/account/login/")
def add_cart_item(request,cartitem_id):
    try:
        cartitem = CartItem.objects.get(id=cartitem_id)
        cartitem.quantity += 1    
        cartitem.save()
    except CartItem.DoesNotExist:
        pass
   
    return redirect(reverse("cart"))


@login_required(login_url="/account/login/")
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


@login_required(login_url="/account/login/")
def remove_cart_item(request, cartitem_id):
    try:
        cartitem = CartItem.objects.get(id = int(cartitem_id))
        cartitem.delete()
    except CartItem.DoesNotExist:
        pass

   
    return redirect(reverse("cart"))


@login_required(login_url="/account/login/")
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

                            cupon.is_used = True
                            cartitem.save()

    context["cartitems"] = cartitems
    print(cartitems)
    return render(request, "shopping/cart.html", context)

                   

@login_required(login_url="/account/login/")
def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)

        product_id = int(data.get("product_id", None))
        size = int(data.get("size", None))
        color = int(data.get("color", None))

        cart = get_cart(request)
        
        product = Product.objects.get(id=product_id)
        cartitems = CartItem.objects.filter(cart=cart, product=product, color__id=color, size__id=size)

        if color == "-1" and size == "-1":
            pass

        elif cartitems.exists(): 
            cartitem = cartitems.first()
            cartitem.quantity += 1  
            cartitem.save()  
            
        else:
            color_obj = ProductColor.objects.get(id=color)
            size_obj = ProductSize.objects.get(id=size)
            cartitem = CartItem(product=product, cart=cart, color=color_obj, size=size_obj)
            cartitem.save()

        return JsonResponse({"cartitems_count": cartitem.quantity})

    return JsonResponse({"oxshadi": "natija"})


@login_required(login_url="/account/login/")
def add_to_wishlist(request, pk, data):
    product = Product.objects.get(id=pk)
    wishlist = Wishlist.objects.filter(user=request.user, product=product)
    if not wishlist.exists():
        wishlist = Wishlist(user=request.user, product=product)
        wishlist.save()

    return redirect(reverse(data))


@login_required(login_url="/account/login/")
def wishlist_items(request):
    items = Wishlist.objects.filter(user=request.user)
    context = {
        "items":items
    }
    return render(request, "shopping/wishlist.html", context)


@login_required(login_url="/account/login/")
def remove_wishlist(request, pk, data):
    product=Product.objects.get(id=pk)
    wishlist_i = Wishlist.objects.filter(user=request.user, product=product)
    try:
        wishlist_i.delete()
    except:
        pass
    
    return redirect(reverse(data))



    


    # try:
    #     wishlist = Wishlist.objects.filter(id=pk)
    #     wishlist.delete()
    # except Wishlist.DoesNotExist:
    #     pass





# def remove(request, cartitem_id):
    
#     data = json.loads(request.body)
#     print(cartitem_id)
#     if request.method == "POST":
#         print(type(cartitem_id))
#         try:
#             print('2')
#             cartitem_id =data.get("cartitem_id", None)
#             print(cartitem_id)

#             cartitem = CartItem.objects.get(id = cartitem_id)
#             cartitem.delete()

#         except Exception as e:
#             print(e)
#             print("ishlamadi")
#             return JsonResponse({"error":"parsing_error"})

#     return JsonResponse({"natija":"o'xshadi"})




            
        
        
        
        


