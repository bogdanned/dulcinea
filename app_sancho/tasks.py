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
            CustomerProductsCreate(customer, product)
            ProductUpdatePrestashop(config, product)

    return products_retrieved
