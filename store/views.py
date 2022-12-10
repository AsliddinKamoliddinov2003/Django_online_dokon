from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

from .models import Category, Product, SubCategory
from .utils import filter_min_max, get_paginated, condition_filter
from shopping.models import CartItem, Cupon
from shopping.utils import get_cart




def home(request):
    products=Product.objects.filter().order_by("-rating")[:12]
 
    context={
        "products": products
    }
    return render(request,"index/index.html",context)


def search(request, products):
    word = request.GET.get('q',None)
    if word:
        return products.filter(Q(translation__title=word) | Q(translation__description=word))
    return None
    

def store(request):
    products = Product.objects.all()
    products = condition_filter(request)

    if search(request, products):
        products=search(request,products)

    paginated = get_paginated(request, products, 3)
    context = {
        "products" : paginated["items"],
        "pages": paginated["pages"],
        "word": products
        }

    return render(request, "store/store.html", context)
    

def category_products(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(sub_category__category=category)
    products=filter_min_max(request,products)

    if search(request, products):
        products=search(request,products)
        
    paginated = get_paginated(request, products, 3)

    context = {
        "products" : paginated["items"],
        "pages": paginated["pages"],
        "word": products
        }
    return render(request, "store/store.html",context)
    

def sub_category_products(request,category_slug,sub_category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory,slug=sub_category_slug, category=category )
    products = Product.objects.filter(sub_category=subcategory)
    products=filter_min_max(request,products)

    if search(request, products):
        products=search(request,products)      
    
    paginated = get_paginated(request, products, 3)

    context = {
        "products" : paginated["items"],
        "pages": paginated["pages"],
        "word": products
        }
    return render(request, "store/store.html",context)


def product_detail(request,slug):
    products = Product.objects.filter(slug=slug)
    if not products.exists():
        return render(reverse("home-page"))
    else:
        product = products.first()

    if request.method == "POST":
        color =  request.POST.get('color',"")
        size =  request.POST.get('size',"")
        cart = get_cart(request) 

        cartitems = CartItem.objects.filter(cart=cart, product=product,color=color,size=size)

        if color == "-1" and size == "-1":
            pass
        elif cartitems.exists():
            cartitem = cartitems.first()
            cartitem.quantity += 1    
            cartitem.save()
        else:
            cartitem = CartItem(product=product, cart=cart,color=color, size=size)
            cartitem.save()
            
    context = {
        "product":product
    }
    return render(request, "store/product_detail.html", context)


def help_page(request):
    return render(request, "index/help.html")


    


    