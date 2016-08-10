from django.contrib import admin
from .models import *
# Register your models here.




class CustomerAdminDatabaseInline(admin.TabularInline):
    model = CustomerDatabase
    fk_name = "customer"

class CustomerAdminStackInline(admin.TabularInline):
    model = CustomerStack
    fk_name = "customer"

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    inlines = [
        CustomerAdminDatabaseInline,
        CustomerAdminStackInline,
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['customer_product_id','name','created','price']
    list_filter = ['category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['customer_category_id','name','customer_parent_category']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerStack)
admin.site.register(CustomerDatabase)
