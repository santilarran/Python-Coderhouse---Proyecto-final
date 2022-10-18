from django.contrib import admin
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView
from AppCoder import views 


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('login/', inicioSesion, name="Login"),
    path('register/', registro, name="Register"),
    path('logout', LogoutView.as_view(template_name="AppCoder/Autenticar/logout.html"), name="Logout"),
    path('editar/', editarUsuario, name="EditarUsuario"),
    path('about/', about, name="About"),
    path('venta/', objetoVenta, name="Venta"),
    path('verobjetos', verObjetos, name="Verobjetos"),
    path('buscar/', buscar, name="Busqueda"),
    path('eliminarObjeto/<objetoNombre>', eliminarObjeto, name="Eliminarobjeto"),
    path('editarObjeto/<objetoNombre>', editarObjeto, name="Editarobjeto"),
]