from dataclasses import fields
from select import select
from django.forms import *

from cliente.models import Clientes, Departamentos, Municipios, TipoDocumento, TipoPersona

class ClienteForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class']='form-control'

    class Meta:
        model=Clientes
        fields='__all__'
        widgets={
        'nombres':TextInput(
            attrs={
                'placeholder': 'Ingrese los nombres',
                'class':'form-control',

            }
        ),
        'apellidos':TextInput(
            attrs={
                'placeholder': 'Ingrese los apellidos',
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
        'nombreContacto':TextInput(
            attrs={
                'placeholder': 'Ingrese un nombre de contacto',
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
        'celularContacto':NumberInput(
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
        'tipoPersonaId':Select(
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

    #Combobox
    tipoPersonaId  = ModelChoiceField(queryset=TipoPersona.objects.all(),label="Tipo persona",widget=Select(
        attrs={'class':'form-control select2',
        'onchange' : "onChageTipopersona();"
    }))
    tipoDocumentoId = ModelChoiceField(queryset=TipoDocumento.objects.all(),label="Tipo documento",widget=Select(
        attrs={'class':'form-control select2',
    }))
    departamentoId = ModelChoiceField(queryset=Departamentos.objects.all(),label="Departamento",widget=Select(
        attrs={'class':'form-control select2',
        'onchange' : "onChageDepartamento();"
    }))
    municipioId = ModelChoiceField(queryset=Municipios.objects.all(),label="Municipio",widget=Select(
        attrs={'class':'form-control select2',
    }))

class SelectTipoPersonaForm(ModelForm):
    class Meta:
        model=TipoPersona
        fields='__all__'
    #Combobox
    tipoPersonaId  = ModelChoiceField(queryset=TipoPersona.objects.all(),label="Tipo persona",widget=Select(
        attrs={'class':'form-control select2',
        'onchange' : "onChageTipopersona();"
    }))
    

class SelectTipoDocumentoForm(ModelForm):
    class Meta:
        model=TipoDocumento
        fields='__all__'
    tipoDocumentoId = ModelChoiceField(queryset=TipoDocumento.objects.all(),label="Tipo documento",widget=Select(
        attrs={'class':'form-control select2',
    }))    

class SelectDepartamentoForm(ModelForm):
    class Meta:
        model=Departamentos
        fields='__all__'
    departamentoId = ModelChoiceField(queryset=Departamentos.objects.all(),label="Departamento",widget=Select(
        attrs={'class':'form-control select2',
        'onchange' : "onChageDepartamento();"
    }))
    municipioId = ModelChoiceField(queryset=Municipios.objects.all(),label="Municipio",widget=Select(
        attrs={'class':'form-control select2',
    }))

class SelectMunicipioForm(ModelForm):
    class Meta:
        model=Municipios
        fields='__all__'
    municipioId = ModelChoiceField(queryset=Municipios.objects.all(),label="Municipio",widget=Select(
        attrs={'class':'form-control select2',
    }))


    
    