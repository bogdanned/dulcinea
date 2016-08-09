from __future__ import unicode_literals

from django.db import models

# Importing Signals
from .signals import *

# Signals functions
def database_product_query_initiated(sender, **kwargs):
    print 'database_product_query_intiated'

def database_product_query_finished(sender, **kwargs):
    print 'database_product_query_finished'

def database_product_query_failed(sender, **kwargs):
    print 'database_product_query_failed'

# Connecting Signals
product_query_initiated.connect(database_product_query_initiated)
product_query_finished.connect(database_product_query_finished)
product_query_failed.connect(database_product_query_failed)


# Product Model
class Product(models.Model):
    #Id of the product in the customer database
    customer_product_id = models.CharField(max_length = 600, null=True, blank = True, verbose_name = 'Customer Product ID')
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank = False, null = False, verbose_name = 'Fecha Creacion')
    customer = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'Cliente')
    price = models.IntegerField(null=True, blank = True, verbose_name = 'Precio')
    discount = models.IntegerField(null=True, blank = True, verbose_name = 'Descuento')
    image_local_path = models.CharField(max_length = 1000, null=True, blank = True, verbose_name = 'Path Local Image')
    name = models.CharField(max_length = 200, null=True, blank = True, verbose_name = 'Name')
    description = models.CharField(max_length = 1000, null=True, blank = True, verbose_name = 'Description')
    category = models.CharField(max_length = 600, null=True, blank = True, verbose_name = 'Categoria')
    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'

    def __unicode__(self):
        return "%s | %s" % (self.name, self.customer)


# Our Customer Info
class Customer(models.Model):
    nr_products = models.IntegerField(null=True, blank = True, verbose_name = 'Nr. Productos')
    name = models.CharField(max_length = 200, null=True, blank = True, verbose_name = 'Name')

    class Meta:
        verbose_name_plural = 'Clientes'
        verbose_name = 'Cliente'

    def __unicode__(self):
        return "%s | %s" % (self.name, self.nr_products)

# The customer Stack Info
class CustomerStack(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    web_language = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'Lenguaje Web')
    web_framework = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'Framework Web')
    #make this a choice field
    database_type = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'Tipo de Base de Datos')

# Customer Database
class CustomerDatabase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = 'DB Customer')
    user = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'DB User')
    password = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'DB Password')
    port = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'DB Port')
    db_type = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'DB Type')
    host = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'DB Host')
    name = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'DB Name')
