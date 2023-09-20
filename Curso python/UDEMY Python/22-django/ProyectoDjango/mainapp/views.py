from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #modulo de formulario para registrar usuario
from mainapp.forms import RegisterForm #formulario personalizado re registro
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout #modulo para el login

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html',{
        "title":"Inicio"
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        "title":"Sobre nosotros"
    })

#login y registro en pagina directa
def register_page(request):
    if request.user.is_authenticated:
        return redirect("inicio")
    else:
        register_form=UserCreationForm() #aqui se puede reemplazar por el form personlizado

        if request.method=="POST":
            register_form=UserCreationForm(request.POST) #aqui se puede reemplazar por el form personlizado
            if register_form.is_valid():
                register_form.save()
                messages.success(request,"Te has registrado existosamente")
                    
                return redirect("inicio")

        return render(request,"users/register.html",{
            "title":"Registro",
            "register_form":register_form
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect("inicio")
    else:
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect("inicio")
            else:
                messages.warning(request,"No te has identificado correctamente")

        return render(request,"users/login.html",{
            "title":"Identificate"
        })

def logout_user(request):
    logout(request)
    return redirect("login")