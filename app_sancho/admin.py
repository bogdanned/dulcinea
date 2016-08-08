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

admin.site.register(Product)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerStack)
admin.site.register(CustomerDatabase)
