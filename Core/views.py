from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from Core.models import ContactUs
from .forms import ContactForm
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _


# @login_required
def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse_lazy('index'))

    context = {
        'form' : form
    }

    return render(request, 'contact.html')



class ContactView(LoginRequiredMixin, CreateView):
    model = ContactUs
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _(f'Welcome To our site {self.request.user.get_username()}'))
        return super().get_success_url()












def about(request):
    return render(request, 'about.html')

def create_story(request):
    return render(request, 'create_story.html')


def index(request):
    return render(request, 'index.html')

