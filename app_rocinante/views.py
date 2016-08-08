from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def ConnectionTest(request):
    title = 'Rocinante'

    context = {
        'products': products,
        'title': title,
    }

    return render(request, 'prestashop.html', context )
