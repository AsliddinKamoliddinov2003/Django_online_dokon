from shopping.views import wishlist_items
from store.models import Category,SubCategory,Product
from shopping.utils import get_cartitems_count
from shopping.models import Cupon, Wishlist



def category(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    daily_products = Product.objects.filter().order_by("-updated_at")[:6]
    max_price = Product.objects.filter().order_by("-price").first()
    cupons = Cupon.objects.all()
    wishlist_items = Wishlist.objects.filter(user=request.user)

    amount = get_cartitems_count(request)

    items = []
    for wi in wishlist_items:
        items.append(wi.product)
    
    return {
        "categories": categories,
        "subcategories":subcategories,
        "daily_products":daily_products,
        "max_price": max_price,
        "cartitems_amount":amount,
        "items":items,
        # "cupons":cupons
    } 