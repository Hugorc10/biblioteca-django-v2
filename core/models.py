from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Author(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Book(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo

class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    livros = models.ManyToManyField(Book, related_name="colecoes")
    colecionador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="colecoes")

    def __str__(self):
        return f"{self.nome} - {self.colecionador.username}"