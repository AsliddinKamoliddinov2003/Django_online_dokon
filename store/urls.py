from django.urls import path
from .views import home, product_detail,store,category_products,sub_category_products, help_page

urlpatterns = [
    path("",home, name="bosh-sahifa"),
    path("store/", store, name="store-page"),
    path("store/<slug:category_slug>/", category_products , name="category-products-page"),
    path("store/<slug:category_slug>/<slug:sub_category_slug>/", sub_category_products, name="subcategory-products-page"),
    path("product/<slug:slug>/", product_detail,name="product-detail"),
    path("Help/", help_page, name="help-page")
]