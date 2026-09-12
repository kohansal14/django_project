from django.urls import path
from . import views


urlpatterns = [
    path('',views.ProductList,name='products-list')
]
