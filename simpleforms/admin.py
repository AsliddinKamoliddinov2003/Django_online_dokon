from django.contrib import admin


from .models import Category, News



class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ["views"]

admin.site.register(Category)
admin.site.register(News,NewsAdmin)
