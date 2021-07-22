from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display=["title", "price", "rating", "sub_category", "is_active"]
    list_display_links=["title"]
    list_editable=["rating","price","is_active"]
    search_fields=["title","description"]
    prepopulated_fields={"slug":("title",)}


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product,ProductAdmin)

