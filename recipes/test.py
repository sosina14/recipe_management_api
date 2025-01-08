from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe

class RecipeAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Test Description",
            ingredients="Test Ingredient",
            instructions="Test Instructions",
            category="Dessert",
            preparation_time=10,
            cooking_time=20,
            servings=2,
            creator=self.user
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Test Recipe")
        self.assertEqual(self.recipe.creator.username, "testuser")

    def test_recipe_list_view(self):
        response = self.client.get('/api/recipes/')
        self.assertEqual(response.status_code, 200)
