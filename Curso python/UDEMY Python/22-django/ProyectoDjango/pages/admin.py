from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

#config extra admin
class PageAdmin(admin.ModelAdmin):
    readonly_fields=("created_at","updated_at")
    search_fields=("title","content")
    list_filter=("visible",)
    list_display=("title","visible","created_at")

#config panel admin
title="Proyecto con Django"
subtitle="Panel de gestión"
admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle

#credenciales para ingresar:
"""
usuario: proyecto
passwd: django2023
"""