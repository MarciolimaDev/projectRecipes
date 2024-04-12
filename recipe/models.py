from os import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#relational database category
class Category(models.Model):
    name = models.CharField(max_length=65) #campo de texto nome da categoria

    def __str__(self):
        return self.name #retorna o nome da categoria

#relational database recipe
class Recipe(models.Model):
    title = models.CharField(max_length=65) #campo de texto
    description = models.CharField(max_length=165) #campo de texto
    slug = models.SlugField() #campo de texto
    preparationTime = models.IntegerField() #tempo de preparo
    preparationTimeUnit = models.CharField(max_length=65) #unidade de medida
    servings = models.IntegerField() #porções
    servingsUnit = models.CharField(max_length=65) #unidade de medida
    preparationSteps = models.TextField() #campo de texto
    preparationStepsIsHTML = models.BooleanField(default=False) #campo de texto em html
    createAt = models.DateTimeField(auto_now_add=True) #cria a data automaticamente no momento da criação
    updateAt = models.DateTimeField(auto_now=True) #atualiza a data automaticamente no momento da atualização
    isPublished = models.BooleanField(default=False) #publicado ou não
    cover = models.ImageField(upload_to='recipe/covers/%Y/%m/%d/') #imagem e o local onde será salva
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) #chave estrangeira da categoria
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #chave estrangeira do usuário


    def __str__(self):
        return self.title #retorna o título da receita


