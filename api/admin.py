from django.contrib import admin

from api.models import Order, Order_item

# Register your models here.
admin.site.register(Order)
admin.site.register(Order_item)