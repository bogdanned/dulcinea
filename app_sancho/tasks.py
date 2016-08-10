from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

from .utils import *

from app_rocinante.connector import *


@task(name="retrieve_customer_products")
def TaskCustomerProductsRetrieve(customer, customer_stack, customer_database, config):
    """Retrieves products from customer database"""
    print 'CustomerProductsRetrieve called'
    products_retrieved = 0
    #Call this in the background with a signal!!
    if customer_stack.web_framework == 'Prestashop':
        products = ProductRetrievePrestashop(config)
        for product in products:
            product = CustomerProductsCreate(customer, product)
    return products_retrieved

@task(name="retrieve_category_products")
def TaskCustomerCategoriesRetrieve(customer, customer_stack, customer_database, config):
    """Retrieves all products categories from customer database"""
    print 'CustomerProductsRetrieve called'
    categories_retrieved = 0
    #Call this in the background with a signal!!
    if customer_stack.web_framework == 'Prestashop':
        categories = CategoriesRetrievePrestashop(config)
        for category in categories:
            category = CustomerCategoriesCreate(customer, category)
    return categories_retrieved


@task(name="update_customer_products")
def TaskCustomerProductsUpdate(customer, customer_stack, customer_database, config):
    #Load all products
    products = Product.objects.filter(customer=customer.id)
    #Updating Product
    for product in products:
        ProductUpdatePrestashop(config, product)

@task(name="update_customer_products_category_relationship")
def TaskCustomerCategoriesProductsUpdate(customer, customer_stack, customer_database, config):
    #Load all products
    products = Product.objects.filter(customer=customer.id)
    categories_products = CategoriesProductPrestashop(config)

    for category_product in categories_products:
        if Product.objects.filter(customer_product_id=category_product['id_product']).exists():
            if Category.objects.filter(customer_category_id=category_product['id_category']).exists():
                product = Product.objects.get(customer_product_id=category_product['id_product'])
                product.category.add(Category.objects.get(customer_category_id=category_product['id_category']))
                product.save()
    """
    print categories_products
    for product in products:
        for category_product in categories_products:
            if product.customer_product_id == category_product['id_product']:
                print 'matched'
                category = Category.objects.get(customer_category_id=category_product['id_category'])
                product.category.add(category)"""
    #Updating Product
    #for product in categories_products:
