from django.contrib import admin
from .models import Category, Product,Subcategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'date']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)

