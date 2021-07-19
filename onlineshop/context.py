from store.models import Category,Product



def doimiy(request):
    categories = Category.objects.all()
    products=Product.objects.all()
   
    return {
        "categories": categories,
        "products":products
    } 