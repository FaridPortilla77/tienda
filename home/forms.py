from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class contacto_form(forms.Form):

    correo =forms.EmailField(widget=forms.TextInput)
    Titulo =forms.CharField(widget=forms.TextInput)
    texto =forms.EmailField(widget=forms.Textarea)

class agregar_producto_form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        exclude = ['status']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))