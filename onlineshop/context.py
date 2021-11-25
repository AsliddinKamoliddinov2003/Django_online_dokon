from store.models import Category,SubCategory,Product
from shopping.utils import get_cartitems_count
from shopping.models import  Wishlist
from django.contrib.auth.decorators import login_required




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
        "cartitems_amount":amount,
    } 

@login_required(login_url="/account/login/")
def user_auth(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)

    items = []
    for wi in wishlist_items:
        items.append(wi.product)

    return {
        "items":items,
    }

