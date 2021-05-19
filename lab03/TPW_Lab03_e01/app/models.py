from django.db import models

# Create your models here.
class Author(models.Model):
    # Dizer ao modelo de dados os atributos existentes e o seu tipo
    name = models.CharField(max_length=70)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    # Representa relacao entre as tabelas :)
    authors = models.ManyToManyField(Author) # rel M:N (na classe que mais necessita da outra)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) # rel 1:M (na classe com M!)
    def __str__(self):
        return self.title
