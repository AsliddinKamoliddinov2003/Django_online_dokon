from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display=["name","created_at","updated_at"]
    list_display_links=["name","created_at","updated_at"]



class ProductAdmin(admin.ModelAdmin):
    list_display=["name","category","price"]
    search_fields=["name","product_description"]



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)


