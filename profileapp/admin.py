from django.contrib import admin

from .models import *

admin.site.register(ClientProfile)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderProduct)