from django.shortcuts import render
from .models import Product
  
def home(request):

    products=Product.objects.filter().order_by("-rating")[:12]
    context={
        "products":products,
    }

    return render(request,"index.html",context)

def product_detail(request,slug):
    return render(request, "product_detail.html")