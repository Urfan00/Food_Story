from django.urls import path
from Recipe.views import recipe_list, recipe_detail, RecipeView, RecipeDetailView



urlpatterns = [
    path('recipe/', RecipeView.as_view(), name='recipe'),
    path('recipe_detail/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
]
