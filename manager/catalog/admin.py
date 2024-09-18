from django.contrib import admin
from .models import Category, Product, ProductCategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductCategory)
class ProductAdmin(admin.ModelAdmin):
    pass
