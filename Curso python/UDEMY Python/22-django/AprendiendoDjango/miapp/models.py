from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=150,verbose_name="Titulo")
    content=models.TextField( verbose_name="Contenido")
    image=models.ImageField(default="null", verbose_name="Miniatura",upload_to="articles")
    public=models.BooleanField(  verbose_name="¿Publicado?")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at=models.DateTimeField(auto_now=True, verbose_name="Modificado")
    #clase meta de django
    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        ordering=["-id"]
    #metodo magico para imprimir objetos en admin
    def __str__(self):
        if self.public:
            public="(Publicado)"
        else:
            public="(Privado)"

        return f"{self.title} {public}"


class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    created_at=models.DateField()
    #clase meta de django
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

"""
###para migrar modelos:
se escribe en ubicacion carpeta: python manage.py makemigrations
###para migrar a tablas sql:
se escribe en cmd: python manage.py sqlmigrate miapp 0001 ------el ultimo es el numero de la carpeta creada en migracion
luego se escribe: python manage.py migrate
"""
