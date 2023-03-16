from django.urls import path
from .views import change_password, forget_password, login, register, reset_password, user_profile



urlpatterns = [
    path('login/', login, name='login'),
    path('change_password/', change_password, name='change_password'),
    path('forget_password/', forget_password, name='forget_password'),
    path('register/', register, name='register'),
    path('reset_password/', reset_password, name='reset_password'),
    path('user_profile/', user_profile, name='user_profile'),
]