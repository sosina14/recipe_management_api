from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Dessert', 'Dessert'),
        ('Main Course', 'Main Course'),
        ('Appetizer', 'Appetizer'),
        ('Breakfast', 'Breakfast'),
        ('Vegetarian', 'Vegetarian'),
    ]
    
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
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


class Rating(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField()  # Ensure this field exists
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} rated {self.recipe.title} - {self.rating}"


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.recipe.title}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} favorited {self.recipe.title}"