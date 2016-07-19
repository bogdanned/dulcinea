from __future__ import unicode_literals

from django.db import models

# Create your models here.


#Customer Model
class Product(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank = False, null = False, verbose_name = 'Fecha Creacion')
    customer = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'Cliente')
    price = models.IntegerField(null=True, blank = True, verbose_name = 'Precio')
    discount = models.IntegerField(null=True, blank = True, verbose_name = 'Descuento')
    image_local_path = models.CharField(max_length = 1000, null=True, blank = True, verbose_name = 'Path Local Image')
    name = models.CharField(max_length = 200, null=True, blank = True, verbose_name = 'Name')
    description = models.CharField(max_length = 1000, null=True, blank = True, verbose_name = 'Description')

    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'

    def __unicode__(self):
        return "%s | %s" % (self.name, self.customer)
