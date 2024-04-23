from django.urls import path
from .views import about, contact, create_story, index, ContactView


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('create_story/', create_story, name='create_story'),
]

