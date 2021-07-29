from django.core.paginator import Paginator




def filter_min_max(request, products):
    min_price = request.GET.get("min", None)
    max_price =  request.GET.get("max",None)
    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price) 
    
    return products 



def get_paginated(request, items, number):
    page = 1

    if request.GET.get("page", None):
        page = request.GET.get("page", None)

    items=filter_min_max(request, items)

    pages = Paginator(items, number)
    items = pages.get_page(page)
    
    paginated = {
        "items": items,
        "pages": pages
    }

    return paginated

