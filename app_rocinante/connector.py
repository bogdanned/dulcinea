#Utilities For Database conection
import mysql.connector
from mysql.connector import errorcode
from app_sancho.models import Product
#Signals
from app_sancho.signals import product_query_initiated
from app_sancho.signals import product_query_finished
from app_sancho.signals import product_query_failed

######################Prestashop Utility###############################

#Query shall be built with language options and categories
#Loads the typical configuration of a Presatshop Ecommerce store
#Future queries will be built based ont his conf

#Input:
# config: configutation array
# query: mysql query to be executed
#Output Products of a prestashop made ecommerce(Prestashop 1.5)
def ProductRetrievePrestashop(config):
    products = [];
    product_query_initiated.send(sender='query initiated')
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        query = ("SELECT ps_product.id_product, ps_product.price FROM ps_product WHERE ps_product.active = 1; ")
        cursor.execute(query)
        #Get all products
        for (id_product, price,) in cursor:
            products.append({'id_product': id_product,
                             'price': price,
                          })
        cursor.close()
        product_query_finished.send(sender='query finished')
        #Get All product Category Names
        print len(products)
        return products
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        error = "Something is wrong with your user name or password!"
        product_query_failed.send(sender=error)
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        error = "Database does not exist!"
        product_query_failed.send(sender=error)
      else:
        print err
        product_query_failed.send(sender=err)
    else:
      cnx.close()
    return products

#ps_product_lang.description, ps_product_lang.description_short, ps_product_lang.name, ps_category_lang.name FROM ps_product INNER JOIN ps_product_lang ON ps_product.id_product = ps_product_lang.id_product INNER JOIN ps_category_product ON ps_product.id_product=ps_category_product.id_product INNER JOIN ps_category_lang ON ps_category_product.id_category=ps_category_lang.id_category

#Updates the produce name, category, description and short description, image path also
def ProductUpdatePrestashop(config, product):
    #1. Retrieve all the products
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT description, description_short, name FROM ps_product_lang WHERE ps_product_lang.id_product= %s " % ( product['id_product']));
    try:
        cursor.execute(query)
        for (description, description_short, name, ) in cursor:
            product.description = description_short
            product.name = name
        product.save()
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        error = "Something is wrong with your user name or password!"
        product_query_failed.send(sender=error)
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        error = "Database does not exist!"
        product_query_failed.send(sender=error)
      else:
        print err
        product_query_failed.send(sender=err)
    else:
      cnx.close()
