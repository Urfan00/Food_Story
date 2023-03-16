from django.shortcuts import render


def login(request):
    return render(request, 'accounts/login.html')


def change_password(request):
    return render(request, 'accounts/change_password.html')


def forget_password(request):
    return render(request, 'accounts/forget_password.html')


def register(request):
    return render(request, 'accounts/register.html')


def reset_password(request):
    return render(request, 'accounts/reset_password.html')


def user_profile(request):
    return render(request, 'user-profile.html')
