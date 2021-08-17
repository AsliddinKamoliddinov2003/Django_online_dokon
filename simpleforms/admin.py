from django.contrib import admin


from .models import  Category, Director, Filial, News



class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ["views"]

admin.site.register(Category)
admin.site.register(News,NewsAdmin)
admin.site.register(Director)
admin.site.register(Filial)