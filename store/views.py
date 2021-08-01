from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.db.models import Q



from .models import Category, Product, SubCategory
from .utils import filter_min_max, get_paginated


  
def home(request):

    products=Product.objects.filter().order_by("-rating")[:12]
    context={
        "products":products
    }

    return render(request,"index.html",context)



def search(request, products):
    word = request.GET.get('q',None)
    if word:
        return products.filter(Q(title__contains=word) | Q(description__contains=word))\
            .exclude(Q(price__gte=2) | Q(rating__lte=3))

    return None






    
def store(request):
    products = Product.objects.all()

    if search(request, products):
        products=search(request,products)


    paginated = get_paginated(request, products, 3)
    context = {
        "products" : paginated["items"],
        "pages": paginated["pages"],
        "word": products
        }

    return render(request, "store.html",context)
    

    

def category_products(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(sub_category__category=category)
    products=filter_min_max(request,products)

    products = Product.objects.all()

    if search(request, products):
        products=search(request,products)
        

    paginated = get_paginated(request, products, 3)

    context = {
        "products" : paginated["items"],
        "pages": paginated["pages"],
        "word": products
        }
    return render(request, "store.html",context)
    



def sub_category_products(request,category_slug,sub_category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory,slug=sub_category_slug, category=category )
    products = Product.objects.filter(sub_category=subcategory)
    products=filter_min_max(request,products)

    products = Product.objects.all()

    if search(request, products):
        products=search(request,products)
        
    
    paginated = get_paginated(request, products, 3)

    context = {
        "products" : paginated["items"],
        "pages": paginated["pages"],
        "word": products
        }
    return render(request, "store.html",context)


def product_detail(request,slug):
    products = Product.objects.filter(slug=slug)
    if not products.exists():
        return render(reverse("home-page"))
    else:
        product = products.first()
    context = {
        "product":product
    }
    return render(request, "product_detail.html", context)

