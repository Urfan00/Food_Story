from django.urls import path
from Recipe.api.views import CategoryAPIView, RecipeListview, RecipeReadUpdateDeleteView


urlpatterns = [
    path('recipes/', RecipeListview.as_view(), name='recipes'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),


    path('recipes/<int:pk>', RecipeReadUpdateDeleteView.as_view(), name='recipes'),
]
