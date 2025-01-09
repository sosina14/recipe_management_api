from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Recipe

class RecipeAPITestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Create a sample recipe
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="A simple test recipe",
            ingredients="Sugar, Milk, Flour",
            instructions="Mix everything",
            category="Dessert",
            preparation_time=10,
            cooking_time=20,
            servings=2,
            creator=self.user,
        )

    def test_create_recipe(self):
        data = {
            "title": "New Recipe",
            "description": "A new recipe description",
            "ingredients": "Eggs, Butter",
            "instructions": "Mix and cook",
            "category": "Breakfast",
            "preparation_time": 15,
            "cooking_time": 30,
            "servings": 4,
        }
        response = self.client.post('/api/recipes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_recipe_list(self):
        response = self.client.get('/api/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_recipe(self):
        data = {
            "title": "Updated Recipe",
            "description": "Updated description",
            "ingredients": "Eggs, Butter, Salt",
            "instructions": "Mix thoroughly and cook",
            "category": "Lunch",
            "preparation_time": 20,
            "cooking_time": 35,
            "servings": 3,
        }
        response = self.client.put(f'/api/recipes/{self.recipe.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_recipe(self):
        response = self.client.delete(f'/api/recipes/{self.recipe.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)