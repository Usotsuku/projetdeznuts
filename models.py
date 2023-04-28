from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField (max_length=200, null=True, blank=True) 
    email = models.CharField (max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Product (models.Model):
    name=models.CharField (max_length=200, null=True, blank=True )
    brand=models.CharField(max_length=200, null=True, blank=True) 
    description=models.TextField(null=True, blank=True)
    price=models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True) 
    countInStock=models.IntegerField(null=True, blank=True, default=0) 
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True) 
    order_date = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100,null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems]) 
        return total
    
    @property
    def get_cart_items (self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems]) 
        return total
    
    def ___str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) 
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) 
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

class CustomerInfo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True) 
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) 
    address = models.CharField(max_length=200, null=False) 
    city = models.CharField(max_length=200, null=False) 
    state = models.CharField(max_length=200, null=False) 
    zipcode = models.CharField(max_length=200, null=False) 

    def ___str__(self):
        return self.address