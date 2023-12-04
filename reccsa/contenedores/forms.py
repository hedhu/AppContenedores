from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import Usuario

class CreacionUsuario(UserCreationForm):
    perfil = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.RadioSelect,
        required=True,
        help_text="Selecciona un tipo de perfil"
    )
    
    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'perfil')