from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def search(request):
    x = request.GET['pcat']
    y = request.GET['pname']
    resc = Product.objects.filter(pcat=x, pname=y)
    return render(request, 'productapp/productstest.html', {'resc': resc })
    # return HttpResponse('products page')
