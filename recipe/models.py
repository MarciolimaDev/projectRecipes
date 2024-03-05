from os import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#relational database category
class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparationTime = models.IntegerField()
    preparationTimeUnit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servingsUnit = models.CharField(max_length=65)
    preparationSteps = models.TextField()
    preparationStepsIsHTML = models.BooleanField()
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    isPublished = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipe/covers/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title


