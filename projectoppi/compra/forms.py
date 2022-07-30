from dataclasses import fields
from datetime import datetime
from select import select
from django.forms import *
from compra.models import *
from proveedores.models import *
from productos.models import Productos

class CompraForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        

    class Meta:
        model=Compra
        fields='__all__'
        widgets={
        'proveedor':Select(
            attrs={
                'class':'form-control select2',

            }
        ),
        'estadoCompra':Select(
            attrs={
                'class':'form-control select2',

            }
        ),        
        'fechaCompra':DateInput(
            format='%Y-%m-%d',
            attrs={
                'value':datetime.now(),
                'class': 'form-control datetimepicker-input',
                'data-target': '#fechaCompra',
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
    
    proveedor = ModelChoiceField(queryset=Proveedores.objects.all(),label="Proveedor",widget=Select(
        attrs={'class':'form-control select2',
    }))
    estadoCompra = ModelChoiceField(queryset=EstadoCompra.objects.all(),label="Estado compra",widget=Select(
        attrs={'class':'form-control select2',
    }))

class DetalleCompraForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model=DetalleCompra
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
        'precioCompra':TextInput(
            attrs={
                'class':'form-control'

            }
        ),
        }
    
    producto = ModelChoiceField(queryset=Productos.objects.all(),label="Producto",widget=Select(
        attrs={'class':'form-control select2',
    }))