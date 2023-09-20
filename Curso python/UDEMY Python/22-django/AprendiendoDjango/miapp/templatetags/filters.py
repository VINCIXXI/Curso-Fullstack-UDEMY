#esto es para crear filtros personalizados
from django import template

register=template.Library()

@register.filter(name="saludo")
def saludo(value):
    return f"<h1 style='background:green'>Bienvenido, </h1>"