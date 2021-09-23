from django import forms
from django.forms import widgets
from django.urls.conf import include
from .models import RegionalUser


class RegionalUserCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegionalUserCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = RegionalUser
        fields = '__all__'
        labels = {
          'name': 'Nombre',
          'last_name': 'Apellido',
          'email': 'Correo electrónico',
          'username': 'Nombre de usuario',
          'password': 'Contraseña',
          'region': 'Región',
          'profile': 'Perfil'
        }
        widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
          'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
          'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}), 
          'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),  
          'password': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),  
          'region': forms.Select(attrs={'class': 'form-select form-select-lg'}),
          'profile': forms.Select(attrs={'class': 'form-select form-select-lg'})

        }