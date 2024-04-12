import re
from django.shortcuts import render, get_list_or_404
from utils.recipes.factory import makeRecipe
# Create your views here.
from recipe.models import Recipe


def home(request):

    recipes = Recipe.objects.all().order_by('-id')

    return render(request, 'recipe/pages/home.html', context={
        'recipes': recipes
    })




def recipe(request, recipe_id):

    recipe = Recipe.objects.filter(
            pk = recipe_id
        ).order_by('-id').first()
    
    return render(request, 'recipe/pages/recipe_view.html', context={
        'recipe': recipe,
        'isDetailPage': True
    })




def category(request, category_id):

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category_id=category_id
        ).order_by('-id')
    )

    return render(request, 'recipe/pages/category.html', context={
        'recipes': recipes,
        'title': f'Categoria | {recipes[0].category.name}'
    })