from dataclasses import fields
from select import select
from django.forms import *
from user.models import User

class UserForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class']='form-control'

    class Meta:
        model=User
        fields='__all__'
        widgets={
        'first_name':TextInput(
            attrs={
                'placeholder': 'Ingrese el nombre',
                'class':'form-control',

            }
        ),

        'last_name':TextInput(
            attrs={
                'placeholder': 'Ingrese el apellido ',
                'class':'form-control',
                
            }
        ),

        'username':TextInput(
            attrs={
                'placeholder': 'Ingrese nombre de usuario ',
                'class':'form-control',
                
            }
        ),
        'email':EmailInput(
            attrs={
                'placeholder': 'Ingrese el correo ',
                'class':'form-control',
                
            }
        ),
        'password':PasswordInput(
            attrs={
                'placeholder': 'Ingrese la contraseña ',
                'class':'form-control',
                
            }
        ),
        }
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                username = self.cleaned_data['username']
                password = self.cleaned_data['password']
                pwd = self.cleaned_data['username']
                form.save()              
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
