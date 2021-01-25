from django.contrib import admin
from .models import Meals, Category, Allergens


@admin.register(Meals)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_editable = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Allergens)
class AllergensAdmin(admin.ModelAdmin):
    list_display = ('name',)
