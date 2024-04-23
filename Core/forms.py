from django import forms
from .models import ContactUs



class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['fullname', 'email', 'subject', 'message']
        # exclude = ['subject']

        widgets = {
            'fullname' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ad/Soyad',
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'E-mail',
                }
            ),
            'subject' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Basliq',
                }
            ),
            'message' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Mesajiniz',
                    'cols' : 30,
                    'rows' : 7
                }
            ),
        }
