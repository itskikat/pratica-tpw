from django.db import models

# Create your models here.

'O ID é automático quando crias as tabelas :p'
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    # password ????????????
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return str(self.name)

class Brand(models.Model):
    name = models.CharField(max_length=70)
    category = models.ManyToManyField(Category)

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    quantity = models.DecimalField(max_digits=3, default=0)
    img = models.URLField()
