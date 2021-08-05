from django.contrib import admin
from .models import *




class ProductImageAdmin(admin.StackedInline):
    model = Product_image
    fields = ["image"]
    extra = 1



class ProductColorStackedAdmin(admin.StackedInline):
    model = Product_color
    fields = ["name"]
    extra = 1



class ProductSizeStackedAdmin(admin.StackedInline):
    model = Product_size
    fields = ["name"]
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display=["title", "price", "rating", "sub_category", "is_active"]
    list_display_links=["title"]
    search_fields=["title","description"]
    prepopulated_fields={"slug":("title",)}

    inlines = [ProductImageAdmin,ProductColorStackedAdmin,ProductSizeStackedAdmin]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}
   



admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Product,ProductAdmin)
