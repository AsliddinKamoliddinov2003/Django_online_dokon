import parler
from intl.models import Person
from django.contrib import admin

from parler import admin as parler_admin

class PersonAdmin(parler_admin.TranslatableAdmin):
    pass


admin.site.register(Person, PersonAdmin)
