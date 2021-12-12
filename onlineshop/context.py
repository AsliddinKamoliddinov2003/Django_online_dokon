from store.models import Category,SubCategory,Product
from shopping.utils import get_cartitems_count
from shopping.models import  Wishlist, CartItem
from django.contrib.auth import authenticate

from shopping.utils import get_cart
from accounts.models import User



def category(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    daily_products = Product.objects.filter().order_by("-updated_at")[:6]
    max_price = Product.objects.filter().order_by("-price").first()
    amount = get_cartitems_count(request)

    return {
        "categories": categories,
        "subcategories":subcategories,
        "daily_products":daily_products,
        "max_price": max_price,
        "cartitems_amount":amount
    }


def user_auth(request):
    items = None
    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user)

        items = []
        for wi in wishlist_items:
            items.append(wi.product)

    return {
        "items": items or []
    }


def all_price(request):
    cart = get_cart(request)
    cartitems = CartItem.objects.filter(cart=cart)
    price_all = 0
    for cartitem in cartitems:
        price_all += ( cartitem.product.price * cartitem.quantity)
 
    return {
        "price_all":price_all
    }


