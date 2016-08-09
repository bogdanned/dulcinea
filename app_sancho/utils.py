#Sanchos's Utilities

from .models import *

#Create a Products imported form customer dtabase
def CustomerProductsCreate(customer, product_data):
    if ProductExists(customer, product_data['id_product']):
        print 'Producto Duplicado'
    else:
        Product.objects.create(customer=customer, price=product_data['price'], customer_product_id=product_data['id_product'] )

#Check if a product is already in Dulcinesa's Database(fast)
def ProductExists(customer, customer_product_id):
    return Product.objects.filter(customer=customer.id, customer_product_id=customer_product_id).exists()
