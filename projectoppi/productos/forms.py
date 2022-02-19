from dataclasses import fields
from select import select
from django.forms import *
from productos.models import TipoProducto, Productos

class TipoProductoForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class']='form-control'

    class Meta:
        model=TipoProducto
        fields='__all__'
        widgets={
        'nombre':TextInput(
            attrs={
                'placeholder': 'Ingrese los nombres',
                'class':'form-control',

            }
        ),

        'descripcion':TextInput(
            attrs={
                'placeholder': 'Ingrese la descripcion ',
                'class':'form-control',

            }
        ),
        }