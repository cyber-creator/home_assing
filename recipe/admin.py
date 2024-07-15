from django.contrib import admin
from .models import Category, Recipe
# Register your models here


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_title', 'image', 'category')
    list_filter = ('category',)
    list_editable = ('category',)
    prepopulated_fields = {'slug': ('recipe_title',)}
