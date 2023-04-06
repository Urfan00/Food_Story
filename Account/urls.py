from django.urls import path
from .views import activate_code, login_view, register_view, logout_view, change_password_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('activate_account/<slug>/', activate_code, name='activate_account'),
    path('change_password/', change_password_view, name='change_password'),
]
