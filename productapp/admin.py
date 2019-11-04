from django.contrib import admin
from .models import Product, Stock

# Register your models here.
# admin.site.register(Product)


class Productadmin(admin.ModelAdmin):
	list_display = ['pid', 'pcat', 'pname', 'pcost', 'pmfdt','pexpt']
	list_filter = ['pcat', 'pmfdt', 'pexpt']

	class meta:
		model = Product
        
admin.site.register(Product, Productadmin)

class Stockadmin(admin.ModelAdmin):
	list_display = ['prodid', 'tot_qty', 'last_update', 'next_update']
	list_filter = ['prodid']
	class meta:
		model = Stock

admin.site.register(Stock, Stockadmin)