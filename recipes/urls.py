from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import RecipeViewSet, RatingViewSet, ReviewViewSet, FavoriteViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('ratings', RatingViewSet, basename='ratings')
router.register('reviews', ReviewViewSet, basename='reviews')
router.register('favorites', FavoriteViewSet, basename='favorites')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('home/', views.home, name='home'),  # Add this line for the root URL
    path('api/', include(router.urls)),  # Group API routes under /api/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('favorites/', views.favorites, name='favorites'),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)