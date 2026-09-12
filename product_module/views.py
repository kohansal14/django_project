from django.shortcuts import render
from .models import Product,ProductCategory,ProductBrand
# Create your views here.


def ProductList(request):
    products = Product.objects.all()
    return render(request,'product_module/product_list.html',context={'products':products})




    
