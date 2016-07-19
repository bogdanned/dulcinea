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
        query = ("SELECT id_product, price, active FROM ps_product ")
        cursor.execute(query)
        for (id_product, price, active) in cursor:
            if (active == 1):
                products.append({'id_product': id_product,
                              'price': price})
        cursor.close()
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
