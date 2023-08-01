from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'price']
    list_filter = ['owner__username']
    readonly_fields = ['slug']



admin.site.register(Product, ProductAdmin)
admin.site.register(ShopCard)