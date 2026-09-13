from django.shortcuts import render
from django.views.generic import ListView

from .models import Product,ProductCategory,ProductBrand
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product_module/product_list.html'
    context_object_name = 'products'





    
