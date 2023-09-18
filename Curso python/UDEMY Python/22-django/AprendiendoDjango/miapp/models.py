from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    image=models.ImageField(default="null")
    public=models.BooleanField( )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    created_at=models.DateField()

"""
###para migrar modelos:
se escribe en ubicacion carpeta: python manage.py makemigrations
###para migrar a tablas sql:
se escribe en cmd: python manage.py sqlmigrate miapp 0001 ------el ultimo es el numero de la carpeta creada en migracion
luego se escribe: python manage.py migrate
"""