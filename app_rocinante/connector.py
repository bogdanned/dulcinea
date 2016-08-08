#Utilities For Database conection
import mysql.connector
from mysql.connector import errorcode

#Signals
from app_sancho.signals import product_query_initiated
from app_sancho.signals import product_query_finished
from app_sancho.signals import product_query_failed

######################Prestashop Utility###############################

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
        query = ("SELECT ps_product.id_product, ps_product.price, ps_product.active, ps_product_lang.description, ps_product_lang.description_short, ps_product_lang.name, ps_category_lang.name FROM ps_product INNER JOIN ps_product_lang on ps_product.id_product = ps_product_lang.id_product INNER JOIN ps_category_product ON ps_product.id_product=ps_category_product.id_product INNER JOIN ps_category_lang ON ps_category_product.id_category=ps_category_lang.id_category; ")
        cursor.execute(query)
        #Get all products
        for (id_product, price, active, description, description_short, name, category_name) in cursor:
            if (active == 1):
                products.append({'id_product': id_product,
                              'price': price,
                              'description': description,
                              'description_short': description_short,
                              'name': name,
                              'category':  category_name,})
        cursor.close()
        product_query_finished.send(sender='query finished')
        #Get All product Category Names
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
