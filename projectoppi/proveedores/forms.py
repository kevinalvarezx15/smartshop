from dataclasses import fields
from select import select
from django.forms import *
from proveedores.models import Proveedores
from cliente.models import TipoDocumento,Departamentos,Municipios,Paises

class ProveedoresForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model=Proveedores
        fields='__all__'
        widgets={
        'nombres':TextInput(
            attrs={
                'placeholder': 'Ingrese los nombres',
                'class':'form-control',

            }
        ),
        'documento':NumberInput(
            attrs={
                'placeholder': 'Ingrese el número de documento',
                'class':'form-control',
                'maxlength':'20',
                'oninput':'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);'

            }
        ),
        'correo':EmailInput(
            attrs={
                'placeholder': 'Ingrese un correo electrónico',
                'class':'form-control',

            }
        ),
        'direccion':TextInput(
            attrs={
                'placeholder': 'Ingrese una dirección',
                'class':'form-control',

            }
        ),  
        'celular':NumberInput(
            attrs={
                'placeholder': 'Ingrese un numero celular',
                'class':'form-control',
                'oninput':'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);'

            }
        ), 
        'tipoDocumentoId':Select(
            attrs={
                'class':'form-control select2',

            }
        ),
        'departamentoId':Select(
            attrs={
                'class':'form-control select2',

            }
        ),
        'municipioId':Select(
            attrs={
                'class':'form-control select2',

            }
        ),
        }
    
    tipoDocumentoId = ModelChoiceField(queryset=TipoDocumento.objects.filter(pais=1),label="Tipo documento",widget=Select(
        attrs={'class':'form-control select2',
    }))
    pais = ModelChoiceField(queryset=Paises.objects.all(),label="País",widget=Select(
        attrs={'class':'form-control select2',
        'onchange' : "onChagePais();"
    }))
    departamentoId = ModelChoiceField(queryset=Departamentos.objects.filter(pais=1),label="Región",widget=Select(
        attrs={'class':'form-control select2',
        'onchange' : "onChageDepartamento();"
    }))
    municipioId = ModelChoiceField(queryset=Municipios.objects.all(),label="Ciudad",widget=Select(
        attrs={'class':'form-control select2',
    }))
