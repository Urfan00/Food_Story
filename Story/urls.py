from django.urls import path
from .views import create_story, recipes, single, stories 


urlpatterns = [
    path('create_story/', create_story, name='create_story'),
    path('recipes/', recipes, name='recipes'),
    path('single/', single, name='single'),
    path('stories/', stories, name='stories'),
]
