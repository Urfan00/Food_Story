from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from services.generator import Generator
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .decorators import not_authorized_user, check_activation_code_time
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

User = get_user_model()


@not_authorized_user
def login_view(request):
    form = LoginForm()
    next_url = request.GET.get('next')

    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # user = authenticate(email=email, password=password) or authenticate(fullname=fullname, password=password)
            user = authenticate(username=username, password=password)

            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('/')
        else:
            print(form.errors)

    context = {
        'form' : form
    }

    return render(request, 'accounts/login.html', context)


def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST or None)

        if form.is_valid():
            new_user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            new_user.set_password(password)
            new_user.is_active = False
            new_user.activation_code = Generator.create_code_for_activate(size=6, model_=User)
            new_user.activation_code_expires_at = timezone.now() + timezone.timedelta(minutes=2)
            new_user.save()

            # send mail part
            send_mail(
                "Activation Code",
                f"Your activation code : {new_user.activation_code}",
                settings.EMAIL_HOST_USER ,
                [new_user.email]
            )

            # login(request, new_user)
            return redirect('activate_account', slug=new_user.slug)
        else:
            print(form.errors)

    context = {
        'form' : form
    }

    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login/')

@check_activation_code_time
def activate_code(request, slug):
    user  = get_object_or_404(User, slug=slug)
    context = {}

    if request.method == 'POST':
        code = request.POST.get('code')
        if code == user.activation_code:
            user.is_active = True
            user.activation_code = None
            user.activation_code_expires_at = None
            user.save()

            login(request, user)
            return redirect('/shop/')
        
    return render(request, 'accounts/activate.html', context)


@login_required(login_url='/')
def change_password_view(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST or None, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect('/')

    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)


def forget_password(request):
    return render(request, 'accounts/forget_password.html')


def reset_password(request):
    return render(request, 'accounts/reset_password.html')


def user_profile(request):
    return render(request, 'user-profile.html')
