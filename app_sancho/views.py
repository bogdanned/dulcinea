from django.shortcuts import render, get_object_or_404
from app_rocinante.connector import ProductRetrievePrestashop
from .models import *
# Create your views here.

# Threading Utils
import threading
from threading import Thread
from multiprocessing import Pool
import time
from functools import partial
#Testing
from django.http import HttpResponse

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


#Check if a product is already in Dulcinesa's Database(fast)
def ProductExists(customer, customer_product_id):
    print 'ProductExists caleld'
    try:
        product = Product.objects.filter(customer=customer.id).get(customer_product_id=customer_product_id)
        return True
    except Product.DoesNotExist:
        return False

#Create a Products imported form customer dtabase
def CustomerProductsCreate(customer, product_data):
    print 'CustomerProductsCreate called'
    print product_data
    print 'Global var customer'
    print customer
    if ProductExists(customer, product_data['id_product']):
        print 'Producto Duplicado'
    else:
        print 'Product creation: '
        product = Product()
        product.customer = 1
        product.name = product_data['name']
        product.price = product_data['price']
        product.category = product_data['category']
        product.description = product_data['description']
        product.save()


def CustomerProductsRetrieve(customer, customer_stack, customer_database, config):
    print 'CustomerProductsRetrieve called'
    products_retrieved = 0
    #Call this in the backgorund with a signal!!

    if customer_stack.web_framework == 'Prestashop':
        products = ProductRetrievePrestashop(config)
        print 'Products Array: '
        print len(products)
        p = Pool(3)
        start = time.time()
        func = partial(CustomerProductsCreate, customer)
        p.map(func, products)
        pool.close()
        pool.join()
        end = time.time()

    return products_retrieved




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

    #Adding Pdoucts to our database
    products_retrieved = CustomerProductsRetrieve(customer, customer_stack, customer_database, config)

    customer = get_object_or_404(Customer, pk=1)
    nr_products = Product.objects.filter(customer=customer.id).count()
    customer.nr_products = nr_products
    customer.save()
    context = {
        'customer_name': customer.name,
        'customer_nr_products': customer.nr_products,
        'message': ' productos actualizados ...'
    }
    return render(request, 'customer.html', context )






def f(x):
    return x*x


def MultiThreadingTest(request):

    num_list = range(1, 500000)

    p = Pool(2)
    start = time.time()
    print(p.map(f, num_list))
    end = time.time()
    print(end - start)

    start2 = time.time()
    for i in num_list:
        print i*i
    end2 = time.time()

    print 'Timeing: '
    print(end - start)

    print(end2 - start2)

    print 'Multi threding test finished'
    return HttpResponse('Test')
