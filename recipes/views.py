from django.shortcuts import render


from rest_framework import viewsets, permissions, filters
from .models import Recipe
from .serializers import RecipeSerializer
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
