from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'recipe/pages/home.html')

def recipe(request, recipe_id):
    return render(request, 'recipe/pages/recipe_view.html')