from django.db import models
from ckeditor.fields import RichTextField #libreria para personalizar los textos a ingresar en admin
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name="Nombre")
    description=models.CharField(max_length=250,verbose_name="Descripcion")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Creado el ")

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self): #metodo magico
        return self.name
    
class Article(models.Model):
    title=models.CharField(max_length=150,verbose_name="Titulo")
    content=RichTextField(verbose_name="Contenido")
    image=models.ImageField(default="null",verbose_name="Imagen",upload_to="articles")
    public=models.BooleanField(verbose_name="¿Publicado?")
    user=models.ForeignKey(User,editable=False,verbose_name="Usuario",on_delete=models.CASCADE) #guarda el id que ha creado el articulo, el CASCADE hace que si se borra el user se borra el articulo
    categories=models.ManyToManyField(Category,verbose_name="Categorias",blank=True) #un articulo puede tener muchas categorias y ademas no es necesario que tenga contenido
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Creado el ")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="Editado el ")

    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        

    def __str__(self): #metodo magico
        return self.title