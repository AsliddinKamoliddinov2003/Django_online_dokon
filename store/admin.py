from django.contrib import admin

from shopping.models import Wishlist
from .models import *


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    fields = ["image"]
    extra = 1



class ProductColorStackedAdmin(admin.StackedInline):
    model = ProductColor
    fields = ["name"]
    extra = 1



class ProductSizeStackedAdmin(admin.StackedInline):
    model = ProductSize
    fields = ["name"]
    extra = 1


class ProductAdmin(admin.ModelAdmin):
#     list_display=["id", "title", "price", "rating", "sub_category", "is_active"]
#     list_display_links=["title"]
#     search_fields=["title","description"]
#     prepopulated_fields={"slug":("title",)}

    inlines = [ProductImageAdmin,ProductColorStackedAdmin,ProductSizeStackedAdmin]


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields={"slug":("name",)}


# class SubCategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields={"slug":("name",)}
   



admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product,ProductAdmin)
admin.site.register(Wishlist)
