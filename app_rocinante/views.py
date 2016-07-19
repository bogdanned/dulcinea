from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .connector import PrestashopProducts

def ConnectionTest(request):
    title = 'Rocinante'

    context = {
        'products': products,
        'title': title,
    }

    return render(request, 'prestashop.html', context )

def RetrieveProducts():
    config = {
      'user': 'root',
      'password': 'root',
      'host': 'localhost',
      'port': '8889',
      'database': 'wobybi',
      'raise_on_warnings': True,
    }
    products =  PrestashopProducts(config)
    return products
