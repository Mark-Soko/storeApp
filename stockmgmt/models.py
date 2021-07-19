from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.lookups import IntegerFieldFloatRounding



class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name =  models.CharField(max_length=50,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=1)
    Buy_price =models.FloatField(default=1)
    image = models.ImageField()
    qty_in_store = models.IntegerField()
    last_updated =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    totalCost= models.FloatField()
    amountPaid =models.FloatField()
    balance = models.FloatField()
    completed = models.BooleanField(default=False)
    last_updated =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)


class Ordereditems(models.Model):
    cart = models.ForeignKey(Order, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    profit = models.FloatField()
    
    
    def __str__(self):
        return self.product.name
    
    
    