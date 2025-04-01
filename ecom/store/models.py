from django.db import models
import datetime


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0,  max_digits=10 , decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField(default=0)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,  max_digits=10 , decimal_places=2)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(blank=True,max_length=100,default=" ")
    phone = models.CharField(max_length=10)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product

