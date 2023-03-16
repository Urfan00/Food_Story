from django.urls import path
from .views import about, contact, homepage



urlpatterns = [
    path('', homepage, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]