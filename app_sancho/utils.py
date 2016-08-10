#Sanchos's Utilities

from .models import *

#Create a Products imported form customer dtabase
def CustomerProductsCreate(customer, product_data):
    if ProductExists(customer, product_data['id_product']):
        print 'Producto Duplicado'
        return False
    else:
        product = Product.objects.create(customer=customer.id,
                                        price=product_data['price'],
                                        customer_product_id=product_data['id_product'], )
        return product


#Check if a product is already in Dulcinesa's Database(fast)
def ProductExists(customer, customer_product_id):
    return Product.objects.filter(customer=customer.id, customer_product_id=customer_product_id).exists()


#Create CATEGORIES imported form customer database
def CustomerCategoriesCreate(customer, category_data):
    #If Category exits UPDATE
    if CategoryExists(customer, category_data['id_category']):
        category = Category.objects.get(customer=customer.id, customer_category_id=category_data['id_category'])
        category.customer_category = category_data['id_category']
        category.description = category_data['description']
        category.name = category_data['name']
        category.customer = customer.id
        category.customer_parent_category = category_data['id_parent']
        category.save()
    #IF Category Does not exists CREATE
    else:
        category = Category.objects.create( customer = customer.id,
                                            customer_category_id = category_data['id_category'],
                                            name = category_data['name'],
                                            description = category_data['description'],
                                            customer_parent_category = category_data['id_parent'],)
        return category

#Check if a product is already in Dulcinesa's Database(fast)
def CategoryExists(customer, customer_category_id):
    return Category.objects.filter(customer=customer.id, customer_category_id=customer_category_id).exists()
