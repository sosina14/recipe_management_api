from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Recipe, Rating, Review
from .serializers import RecipeSerializer, RatingSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RecipeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Recipe instances.
    """
    queryset = Recipe.objects.all().order_by('-created_date')
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'ingredients', 'category']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        recipe_id = request.data.get('recipe')

        # Prevent duplicate ratings by the same user for the same recipe
        if Rating.objects.filter(user=user, recipe_id=recipe_id).exists():
            return Response({'detail': 'You have already rated this recipe.'},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def add_to_favorites(self, request):
        recipe_id = request.data.get('recipe')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        
        request.user.favorite_set.create(recipe=recipe)
        return Response({'detail': 'Recipe added to favorites.'})

    @action(detail=False, methods=['delete'])
    def remove_from_favorites(self, request):
        recipe_id = request.data.get('recipe')
        favorite = request.user.favorite_set.filter(recipe_id=recipe_id).first()
        
        if favorite:
            favorite.delete()
            return Response({'detail': 'Recipe removed from favorites.'})
        
        return Response({'detail': 'Favorite not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def list_favorites(self, request):
        favorites = request.user.favorite_set.all()
        serializer = RecipeSerializer([fav.recipe for fav in favorites], many=True)
        return Response(serializer.data)
    




from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Home View - List Recipes
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

# Recipe Detail View
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.ingredients.split(',')
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})

# Favorites View (Optional)
def favorites(request):
    # Add logic to fetch the user's favorite recipes
    return render(request, 'favorites.html')
