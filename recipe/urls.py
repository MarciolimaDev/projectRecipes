from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('recipe/<int:recipe_id>/', views.recipe)
]