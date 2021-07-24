from store.models import Category,SubCategory,Product



def category(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    daily_products = Product.objects.filter().order_by("-updated_at")[:6]
    max_price = Product.objects.filter().order_by("-price").first().price
   
    return {
        "categories": categories,
        "subcategories":subcategories,
        "daily_products":daily_products,
        "max_price": max_price
    } 