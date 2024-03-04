from django.shortcuts import render
from utils.recipes.factory import makeRecipe
# Create your views here.


def home(request):
    return render(request, 'recipe/pages/home.html', context={
        'recipes': [makeRecipe() for _ in range(10)]
    })

def recipe(request, recipe_id):
    return render(request, 'recipe/pages/recipe_view.html', context={
        'recipe': makeRecipe(),
        'isDetailPage': True
    })