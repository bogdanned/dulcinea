from django.shortcuts import render, get_object_or_404
from app_rocinante.connector import ProductRetrievePrestashop
from .models import *
# Create your views here.

from .tasks import TaskCustomerProductsRetrieve

def SanchoAdminDashboard(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }

    return render(request, 'admin_dashboard.html', context )


def CustomerGeneralView(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
        'customer': customer,
        'message': ' ',
    }

    return render(request, 'customer.html', context )


def CustomerProductsUpdate(request, customer_pk):
    #Loading Customer Info
    customer = get_object_or_404(Customer, pk=customer_pk)
    customer_database = get_object_or_404(CustomerDatabase, customer=customer_pk)
    customer_stack = get_object_or_404(CustomerStack, customer=customer_pk)

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
    print 'Task called'
    TaskCustomerProductsRetrieve.delay(customer=customer, customer_stack=customer_stack, customer_database=customer_database, config=config)

    customer = get_object_or_404(Customer, pk=1)
    nr_products = Product.objects.filter(customer=customer.id).count()
    customer.nr_products = nr_products
    customer.save()
    context = {
        'customer': customer,
        'message': ' productos actualizados ...'
    }
    return render(request, 'customer.html', context )
