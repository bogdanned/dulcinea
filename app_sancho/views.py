from django.shortcuts import render, get_object_or_404
from app_rocinante.views import RetrieveProducts
from .models import Customer, Product
# Create your views here.


def CustomerGeneralView(request):
    customer = get_object_or_404(Customer, pk=1)
    nr_products = Product.objects.filter(customer=customer.id).count()

    context = {
        'customer_name': customer.name,
        'customer_nr_products': nr_products,
        'message': ' ',

    }

    return render(request, 'customer.html', context )


def CustomerProductsUpdate(request):

    products_retrieved = 0;
    products = RetrieveProducts()
    for product_data in products:
        product = Product()
        product.customer = 1
        product.name = product_data['name']
        product.price = product_data['price']
        product.category = product_data['category']
        product.description = product_data['description']
        product.save()
        products_retrieved += 1;
    customer = get_object_or_404(Customer, pk=1)
    nr_products = Customer.objects.filter(customer=customer.id).count()

    context = {
        'customer_name': customer.name,
        'customer_nr_products': nr_products,
        'message': products_retrieved + ' productos actualizados ...'
    }
    return render(request, 'customer.html', context )
