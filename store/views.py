from django.shortcuts import render
from .models import Product
from django.shortcuts import get_list_or_404
  
def home(request):

    products=Product.objects.filter().order_by("-rating")[:12]
    context={
        "products":products,
    }

    return render(request,"index.html",context)

def product_detail(request,slug):
    product = get_list_or_404(Product, slug=slug)
    context = {
        "product":product
    }
    return render(request, "product_detail.html", context)