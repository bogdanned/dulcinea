from django.shortcuts import render, get_object_or_404
from app_rocinante.connector import ProductRetrievePrestashop
from .models import *
# Create your views here.

from .tasks import *

def SanchoAdminDashboard(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }

    return render(request, 'admin_dashboard.html', context )


def CustomerGeneralView(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    customer_database = get_object_or_404(CustomerDatabase, customer=customer_pk)
    customer_stack = get_object_or_404(CustomerStack, customer=customer_pk)

    #Context Info
    context = {
        'customer': customer,
        'customer_database': customer_database,
        'customer_stack': customer_stack,
        'message': '',
    }

    return render(request, 'customer.html', context )


def CustomerProductsCreate(request, customer_pk):
    #Loading Customer Info
    customer = get_object_or_404(Customer, pk=customer_pk)
    customer_database = get_object_or_404(CustomerDatabase, customer=customer_pk)
    customer_stack = get_object_or_404(CustomerStack, customer=customer_pk)

    #Context Info
    context = {
        'customer': customer,
        'customer_database': customer_database,
        'customer_stack': customer_stack,
        'message': '',
        'title': 'Obtener Productos'
    }

    #Retrieving Products
    products_retrieved = 0;
    #Database Configuration
    config = {
      'user': customer_database.user,
      'password': customer_database.user,
      'host': customer_database.host,
      'port': customer_database.port,
      'database': customer_database.name,
      'raise_on_warnings': True,
    }

    #Adding Proucts to our database by means of signals
    #Give the cutomer an estimated time: When creation completed refresh the page_missing
    #Handle my Sql errors better
    # Copy teh products foto to predefined folders
    TaskCustomerProductsRetrieve.delay(customer=customer, customer_stack=customer_stack, customer_database=customer_database, config=config)
    TaskCustomerCategoriesRetrieve.delay(customer=customer, customer_stack=customer_stack, customer_database=customer_database, config=config)

    nr_products = Product.objects.filter(customer=customer.id).count()
    customer.nr_products = nr_products
    customer.save()

    return render(request, 'customer.html', context )


def CustomerProductsUpdate(request, customer_pk):
    #Loading Customer Info
    customer = get_object_or_404(Customer, pk=customer_pk)
    customer_database = get_object_or_404(CustomerDatabase, customer=customer_pk)
    customer_stack = get_object_or_404(CustomerStack, customer=customer_pk)

    #Context Info
    context = {
        'customer': customer,
        'customer_database': customer_database,
        'customer_stack': customer_stack,
        'message': '',
    }

    #Retrieving Products
    products_retrieved = 0;
    #Database Configuration
    config = {
      'user': customer_database.user,
      'password': customer_database.user,
      'host': customer_database.host,
      'port': customer_database.port,
      'database': customer_database.name,
      'raise_on_warnings': True,
    }

    #Adding Proucts to our database by means of signals
    #Give the cutomer an estimated time: When creation completed refresh the page_missing
    #Handle my Sql errors better
    # Copy teh products foto to predefined folders
    TaskCustomerProductsUpdate.delay(customer=customer, customer_stack=customer_stack, customer_database=customer_database, config=config)
    TaskCustomerCategoriesProductsUpdate.delay(customer=customer, customer_stack=customer_stack, customer_database=customer_database, config=config)

    nr_products = Product.objects.filter(customer=customer.id).count()
    customer.nr_products = nr_products
    customer.save()

    return render(request, 'customer.html', context )


def CustomerProductsView(request, customer_pk):
    #Loading Customer Info
    customer = get_object_or_404(Customer, pk=customer_pk)
    customer_database = get_object_or_404(CustomerDatabase, customer=customer_pk)
    customer_stack = get_object_or_404(CustomerStack, customer=customer_pk)
    products = Product.objects.filter(customer=customer.id)

    #Context Info
    context = {
        'customer': customer,
        'customer_database': customer_database,
        'customer_stack': customer_stack,
        'message': '',
        'title': 'Lista Productos',
        'products': products,
    }


    return render(request, 'customer_products.html', context)
