from django.db import models


# Create your models here.

# class User(models.Model):
#     user_name = models.CharField(max_length=200,null=False,blank=False)
#     phone_number = models.CharField(max_length=20,null=False,blank=False)
#     password = models.CharField(max_length=50,null=False,blank=False)
    
#     def __str__(self):
#         return self.user_name
    
    
# class Product(models.Model):
#     product_name = models.CharField(max_length=200,null=False,blank=False)
#     price = models.DecimalField(max_digits=10,decimal_places=4)
#     quantity = models.IntegerField()
#     qom = models.CharField(max_length=200,null=False,blank=False)
#     stock = models.IntegerField()
#     barcode = models.CharField(max_length=200,null=False,blank=False)
#     weight = models.IntegerField()
    
#     def __str__(self):
#         return self.product_name
    
class Order(models.Model):
    # user =models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    order_total = models.DecimalField(max_digits=10,decimal_places=4)
    weight_total = models.DecimalField(max_digits=10,decimal_places=4)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.order_id
    
    
class Order_item(models.Model):
    # product =models.ForeignKey(Product, on_delete=models.CASCADE,related_name= ,null=True,blank=True)
    orders =models.ForeignKey(Order, on_delete=models.CASCADE,related_name='user_orders',null=True,blank=True)
    p_name = models.CharField(max_length=200,null=False,blank=False)
    p_price = models.DecimalField(max_digits=10,decimal_places=4)
    p_quantity = models.IntegerField()
    p_stock = models.IntegerField()
    p_barcode = models.CharField(max_length=200,null=False,blank=False)
    p_weight = models.IntegerField()
    
    
    def __str__(self):
        return self.order_id
    
