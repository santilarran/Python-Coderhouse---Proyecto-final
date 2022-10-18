from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import ObjetoVenta



class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)

    class Meta:

        model = User 
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]



class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Nueva Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Nueva contraseña", widget = forms.PasswordInput)

    class Meta:

        model = User 
        fields = ["email", "first_name", "last_name", "password1", "password2"]


class ObjetoFormulario(forms.ModelForm):

    class Meta:

        model = ObjetoVenta
        fields = ["nombre","apellido","contacto","objeto", "descripcion", "fecha", "precio", "imagen"]