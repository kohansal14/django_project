from django.contrib import admin
from . models import Product,ProductCategory,ProductBrand
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(ProductBrand)

admin.site.register(ProductCategory)