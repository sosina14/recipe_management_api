from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_date', 'creator')  # Update to use created_date
    list_filter = ('category', 'created_date')  # Update to use created_date
    search_fields = ('title', 'description', 'ingredients')

admin.site.register(Recipe, RecipeAdmin)