from django import forms
from django.core import validators #libreria para validar errores

class FormArticle(forms.Form):
    title=forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={ #para personalizarlos más
                "placeholder":"Mete el titulo",
                "class":"titulo_form"
            }
        ),
        validators=[
            validators.MinLengthValidator(4, "el titulo es demasiado corto"),
            validators.RegexValidator("^[A-Za-z0-9 ]*$", "El titulo está mal formado","invalid_title")
        ]
    )

    content=forms.CharField(
        label="Contenido",
        widget=forms.Textarea
    )
    #tambien se pueden personalizar asi:
    """
    content.widget.attrs.update({
        "placeholder":"Mete el titulo",
        "class":"titulo_form"
    })"""

    public_options=[
        (0, "No"),
        (1, "Si")
    ]
    public=forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_options
    )