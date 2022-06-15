from django.contrib import admin

from api.models import Order, Order_item,User

# Register your models here.
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(User)