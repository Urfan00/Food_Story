from django.shortcuts import redirect, render
from .models import User
from .forms import ChangePasswordForm, CustomSetPasswordForm, LoginForm, RegistrationForm, ResetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes
from .tokens import account_activation_token
from django.core.mail import send_mail
from Food_story.settings import EMAIL_HOST_USER
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView


def logout_view(request):
    logout(request)
    return redirect('login_page')


def login_view(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f'Welcome To our site {user.get_username()}')
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Your username or password wrong!')

    context = {
        'form' : form
    }

    return render(request, 'login.html', context)


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login_page')

    def form_valid(self, form):
        user = form.save()

        subject = 'Activate your account'
        current_site = get_current_site(self.request)
        message = render_to_string('confirmation_email.html', {
            'user' : user,
            'domain': current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
            'token' : account_activation_token.make_token(user)
        })
        from_email = EMAIL_HOST_USER
        to_email = self.request.POST['email']
        send_mail(subject, message, from_email, [to_email, ])

        return super().form_valid(form)


def activate(requset, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(requset, 'Your profile is activated')
        user.is_active = True
        user.save()
        return redirect('login_page')
    else:
        messages.error(requset, 'Your session is expired')
        return redirect('/')


class ChangePasswordView(PasswordChangeView):
    template_name='change_password.html'
    form_class= ChangePasswordForm
    success_url = reverse_lazy('login_page')


class ResetPasswordView(PasswordResetView):
    template_name = 'reset/forget_password.html'
    form_class = ResetPasswordForm
    email_template_name = 'reset/reset_password_email.html'
    subject_template_name = 'reset/reset_password_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      "If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."

    success_url = reverse_lazy('login_page')


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name='reset/reset_password_confirm.html'
    form_class=CustomSetPasswordForm
    success_url = reverse_lazy('reset_password_complete')
