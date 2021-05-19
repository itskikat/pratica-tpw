from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    telephone = models.IntegerField()
    fax = models.IntegerField()
    nacionality = models.CharField(max_length=20)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1)
    # Representa relacao entre as tabelas :)
    work_exp = models.ManyToManyField(Author) # rel M:N (na classe que mais necessita da outra)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) # rel 1:M (na classe com M!)
    def __str__(self):
        return self.name

class Employer(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    business_sector = models.CharField(max_length=50)

class Position(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    worker = models()