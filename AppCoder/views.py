from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user:

                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido {user}"})

            else:

                return render(request, "AppCoder/inicio.html", {"mensaje": "Datos incorrectos"})

    else:

        form = AuthenticationForm()

    return render(request, "AppCoder/Autenticar/login.html", {"formulario": form})


def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Usuario creado"})

    else:

        form = UsuarioRegistro()

    return render(request, "AppCoder/Autenticar/register.html", {"formulario": form})


@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form = FormularioEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
        })

    return render(request, "AppCoder/Autenticar/editarPerfil.html", {"formulario": form, "usuario": usuario})


def inicio(request):

    return render(request, 'AppCoder/inicio.html')


def about(request):

    return render(request, 'AppCoder/about.html')


@login_required
def objetoVenta(request):

    if request.method == "POST":

        formulario1 = ObjetoFormulario(request.POST, request.FILES)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            objeto1 = ObjetoVenta(nombre=info["nombre"],apellido=info["apellido"],contacto=info["contacto"],objeto=info["objeto"], descripcion=info["descripcion"],
                                  fecha=info["fecha"], precio=info["precio"], imagen=info["imagen"])

            objeto1.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        formulario1 = ObjetoFormulario()

    return render(request, 'AppCoder/Autenticar/añadirVenta.html', {"form": formulario1})


def verObjetos(request):

    objetos = ObjetoVenta.objects.all()

    contexto = {"objects": objetos}

    return render(request, 'AppCoder/verObjetos.html', contexto)


def buscar(request):

    if request.GET["objeto"]:

        objeto = request.GET["objeto"]

        resultados = ObjetoVenta.objects.filter(objeto__icontains=objeto)

        return render(request, "AppCoder/busqueda.html", {"resultados": resultados, "busqueda": objeto})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)

@login_required
def eliminarObjeto(request, objetoNombre):

    objeto1 = ObjetoVenta.objects.get(objeto=objetoNombre)

    objeto1.delete()

    objetos1 = ObjetoVenta.objects.all()

    contexto = {"resultados": objetos1}

    return render(request, "AppCoder/verObjetos.html", contexto)

@login_required
def editarObjeto(request, objetoNombre):

    objeto1 = ObjetoVenta.objects.get(objeto=objetoNombre)

    if request.method == "POST":

        formulario1 = ObjetoFormulario(request.POST, request.FILES)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            objeto1.nombre = info["nombre"]
            objeto1.apellido = info["apellido"]
            objeto1.contacto = info["contacto"]
            objeto1.objeto = info["objeto"]
            objeto1.descripcion = info["descripcion"]
            objeto1.fecha = info["fecha"]
            objeto1.precio = info["precio"]
            objeto1.imagen = info["imagen"]
            
            objeto1.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        formulario1 = ObjetoFormulario(initial={"nombre":objeto1.nombre,"apellido":objeto1.apellido,"contacto":objeto1.contacto,"objeto":objeto1.objeto, "descripcion":objeto1.descripcion, "fecha":objeto1.fecha, "precio":objeto1.precio, "imagen":objeto1.imagen})

    return render(request, 'AppCoder/editarObjeto.html', {"form": formulario1, "resultado":objetoNombre})
