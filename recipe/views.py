from django.shortcuts import render
from utils.recipes.factory import makeRecipe
# Create your views here.
from recipe.models import Recipe


def home(request):

    recipes = Recipe.objects.all().order_by('-id')

    return render(request, 'recipe/pages/home.html', context={
        'recipes': recipes
    })

def recipe(request, recipe_id):
    return render(request, 'recipe/pages/recipe_view.html', context={
        'recipe': makeRecipe(),
        'isDetailPage': True
    })


def category(request, category_id):

    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')

    return render(request, 'recipe/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category |'
    })