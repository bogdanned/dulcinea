#Utilities For Database conection
import mysql.connector
from mysql.connector import errorcode

######################Prestashop Utility###############################

#Input:
# config: configutation array
# query: mysql query to be executed
def PrestashopProducts(config):
    products = [];
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
        #Get All product Category Names
        return products
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cnx.close()
    return products
