from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return render(request,'home_module/index.html')



def site_header_component(request):
    return render(request,'header_component.html')


def site_footer_component(request):
    return render(request,'footer_component.html')