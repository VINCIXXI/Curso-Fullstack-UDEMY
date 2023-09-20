from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=("created_at","updated_at")

#estos modelos se visualizan en la interfaz de admin de django
admin.site.register(Article, ArticleAdmin) 
admin.site.register(Category)

#config titulo panel
#admin.site.site_header="title"
#cambiar el titulo pestaña
#admin.site.site_title="title"
#admin.site.index_title="sitio administrativo"
