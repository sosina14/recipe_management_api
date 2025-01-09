from rest_framework import serializers
from .models import Recipe, Rating, Review

class RecipeSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients', 'instructions',
                  'category', 'prep_time', 'cook_time', 'servings',
                  'created_date', 'image', 'creator']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'recipe', 'user', 'rating', 'created_date']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'recipe', 'user', 'review', 'created_date']

from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'recipe', 'user', 'rating', 'created_at']  # Include 'rating' here