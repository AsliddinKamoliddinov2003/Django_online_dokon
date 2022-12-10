from django.contrib import admin

from shopping.models import Wishlist
from .models import *

from parler.admin import TranslatableStackedInline, TranslatableAdmin


class SlugableAdmin:
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    fields = ["image"]
    extra = 1



class ProductColorStackedAdmin(TranslatableStackedInline):
    model = ProductColor
    fields = ["name"]
    extra = 1



class ProductSizeStackedAdmin(TranslatableStackedInline):
    model = ProductSize
    fields = ["name"]
    extra = 1


class ProductAdmin(TranslatableAdmin, SlugableAdmin):
    list_display=["id", "title", "price", "rating", "sub_category", "is_active"]
    list_display_links=["title"]
    list_editable = ["price", "rating", "is_active"]
    search_fields=["title","description"]

    inlines = [ProductImageAdmin,ProductColorStackedAdmin,ProductSizeStackedAdmin]


class CategoryAdmin(TranslatableAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }


class SubCategoryAdmin(TranslatableAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }
   


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Wishlist)
