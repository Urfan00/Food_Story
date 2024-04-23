from django.urls import path
from django.contrib.auth.views import PasswordResetCompleteView

from .views import ChangePasswordView, CustomLoginView, RegisterView, ResetPasswordConfirmView, ResetPasswordView, login_view, logout_view, activate


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name = 'register'),

    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),

    path('logout/', logout_view, name = 'logout'),

    path('change_password/', ChangePasswordView.as_view(), name='change_password'),

    path('reset_password/', ResetPasswordView.as_view(), name = 'reset_password'),
    path('reset_password_confirm/<str:uidb64>/<str:token>/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='reset/reset_password_complete.html'),name='reset_password_complete'),
    
]
