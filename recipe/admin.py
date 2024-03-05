from django.contrib import admin
from .models import Category, Recipe
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ...

#maneira 2
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

#maneira 1
admin.site.register(Category, CategoryAdmin)