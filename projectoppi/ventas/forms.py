from dataclasses import fields
from datetime import datetime
from select import select
from django.forms import *
from ventas.models import *
from proveedores.models import *
from productos.models import Productos
from cliente.models import *


class VentaForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        

    class Meta:
        model=Venta
        fields='__all__'
        widgets={
        'cliente':Select(
            attrs={
                'class':'form-control select2',

            }
        ),
        'estadoVenta':Select(
            attrs={
                'class':'form-control select2',

            }
        ),        
        'fechaVenta':DateInput(
            format='%Y-%m-%d',
            attrs={
                'value':datetime.now(),
                'class': 'form-control datetimepicker-input',
                'data-target': '#fechaVenta',
                'data-toggle': 'datetimepicker',
                'autocomplete': 'off',
                'id': 'fechaCompra',

            }
        ),
        'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }
    
    cliente = ModelChoiceField(queryset=Clientes.objects.all(),label="Cliente",widget=Select(
        attrs={'class':'form-control select2',
    }))
    estadoVenta = ModelChoiceField(queryset=EstadoVenta.objects.all(),label="Estado venta",widget=Select(
        attrs={'class':'form-control select2',
    }))

class DetalleVentaForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model=DetalleVenta
        fields='__all__'
        widgets={
        'producto':Select(
            attrs={
                'class':'form-control select2',

            }
        ),
        'Cantidad':NumberInput(
            attrs={
                'class':'form-control select2',

            }
        ),        
        'precioVenta':TextInput(
            attrs={
                'class':'form-control'

            }
        ),
        }
    
    producto = ModelChoiceField(queryset=Productos.objects.all(),label="Producto",widget=Select(
        attrs={'class':'form-control select2',
    }))

