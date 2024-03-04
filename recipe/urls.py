from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe-detail')
]