from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Dessert', 'Dessert'),
        ('Main Course', 'Main Course'),
        ('Appetizer', 'Appetizer'),
        ('Breakfast', 'Breakfast'),
        ('Vegetarian', 'Vegetarian'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()  # Comma-separated list of ingredients
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    preparation_time = models.IntegerField()  # in minutes
    cooking_time = models.IntegerField()  # in minutes
    servings = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.title
    

    
