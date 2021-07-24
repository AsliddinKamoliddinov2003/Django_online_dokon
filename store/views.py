from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404

  
def home(request):

    products=Product.objects.filter().order_by("-rating")[:12]
    context={
        "products":products,
    }

    return render(request,"index.html",context)


def store(request):
    products=Product.objects.all()
    context = {
        "products":products
    }
    return render(request, "store.html",context)


def category_products(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(sub_category__category=category)
    context = {
        "products":products
    }
    return render(request, "store.html",context)


def sub_category_products(request,category_slug,sub_category_slug):
    return render(request, "store.html")


def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        "product":product
    }
    return render(request, "product_detail.html", context)