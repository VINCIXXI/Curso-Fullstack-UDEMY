from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required #modeulo importado 

# Create your views here.
@login_required(login_url="login") #esto hace que si quiere visualizar esta interfaz primero ingrese si no ha ingresado
def page(request,slug):

    page=Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
        "page":page
    }) #se coloca render porque es una vista