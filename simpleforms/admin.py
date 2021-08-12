from django.contrib import admin


from .models import Actor, Category, Director, Filial, Movie, News



class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ["views"]

admin.site.register(Category)
admin.site.register(News,NewsAdmin)
admin.site.register(Director)
admin.site.register(Filial)
admin.site.register(Actor)
admin.site.register(Movie)