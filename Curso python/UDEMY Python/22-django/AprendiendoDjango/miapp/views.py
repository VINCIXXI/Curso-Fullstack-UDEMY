from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages #para importar los mensajes flash

# Create your views here.

layout="""
    <h1>Sitio web con Django | David Rodriguez</h1>
    <hr>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola Mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Pagina de Pruebas</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
"""

#METODOS que vamos a poner en urls.py

def index(request):
    """
    html= aqui se puede escribir codigo html tambien y llamarla en el return
    """

    nombre="David Rodriguez"
    lenguajes=["js","PHP","C"]

    return render(request,"index.html",{
        'title':"Inicio",
        'mi_variable': "Soy un dato que esta en la vista",
        'nombre':nombre,
        'lenguajes':lenguajes
    })#se usa para importa el codigo en html

def hola_mundo(request): #parametro que siempre debe ir
    return render(request,"hola_mundo.html")

def pagina(request,redirigir=0):
    if redirigir==1:
        return redirect("contacto",nombre="David")

    return render(request, "pagina.html")

def contacto(request,nombre=""): #para tener parametros opcionales es ""
    return HttpResponse(layout+f"<h2>Contacto {nombre}</h2>")


def crear_articulo(request,title,content,public):
    articulo=Article(
        title=title,
        content=content,
        public=public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title}")

def articulo(request):
    articulo=Article.objects.get(title="Superman",public=False) # get permite sacar  un dato
    return HttpResponse(f"Articulo: {articulo.title}")

def editar_articulo(request,id):
    articulo=Article.objects.get(pk=id)
    articulo.title="Batman"
    articulo.content="pelicula del 2017"
    articulo.public=True

    articulo.save()

    return HttpResponse(f"Articulo editado: {articulo.title}")

def articulos(request):
    articulos=Article.objects.all()
    #articulos=Article.objects.order_by("title")

    #articulos=Article.objects.raw("SELECT") #para hacer consultas en SQL

    return render(request,"articulos.html",{
        "articulos":articulos
    })

def borrar_articulo(reques, id):
    articulo=Article.objects.get(pk=id)
    articulo.delete()

    return redirect("articulos")


def save_article(request):
    """
    if request.method=="GET":
        title=request.GET['title'] #datos en GET son visibles en url y son vulnerables
        content=request.GET['content']
        public=request.GET['public']
    """
    if request.method=="POST":
        title=request.POST['title'] 
        content=request.POST['content']
        public=request.POST['public']

        articulo=Article(
            title=title,
            content=content,
            public=public
        )
        articulo.save()
        return HttpResponse(f"Articulo creado: {articulo.title} {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido cargar el articulo</h2>")

def create_article(request):
    return render(request,"create_article.html")


def create_full_article(request):
    if request.method=="POST":
        formulario=FormArticle(request.POST)
        if formulario.is_valid():
            data_form=formulario.cleaned_data
            
            title=data_form.get("title")
            content=data_form["content"]
            public=data_form["public"]

            articulo=Article(
            title=title,
            content=content,
            public=public
            )
            articulo.save()

            #crea mensaje flash: sesion que se muestra por una actualizacion de pantalla
            messages.success(request,f"Has creado correctamente el articulo {articulo.id}")

            return redirect("articulos")
            # return HttpResponse(articulo.title+" -"+articulo.content+" -"+str(articulo.public))
    else:
        formulario=FormArticle()
    return render(request, "create_full_article.html",{
        'form':formulario
    })