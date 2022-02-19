from django.db import models
from datetime import datetime

# Create your models here.
class Paises(models.Model):
    nombre=models.CharField(max_length=50,verbose_name='Nombre')
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table="tblPaises"
class TipoPersona(models.Model):
    nombre=models.CharField(max_length=50,verbose_name='Nombre')
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table="tblTipoPersona"
        
class TipoDocumento(models.Model):
    nombre=models.CharField(max_length=50,verbose_name='Nombre')
    TipoPersonaId=models.ForeignKey(TipoPersona,verbose_name='Tipo persona',on_delete=models.PROTECT,null=True,blank=True)
    pais=models.ForeignKey(Paises,verbose_name='Paises',on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table="tblTipoDocumento"
      
class Departamentos(models.Model):
    nombre=models.CharField(max_length=50,verbose_name='Nombre')
    pais=models.ForeignKey(Paises,verbose_name='Paises',on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table="tblDepartamentos"

class Municipios(models.Model):
    nombre=models.CharField(max_length=50,verbose_name='Nombre')
    DepartamentoId=models.ForeignKey(Departamentos,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table="tblMunicipios"

class Clientes(models.Model):
    documento=models.BigIntegerField(verbose_name='Número documento',primary_key=True)
    nombres=models.CharField(max_length=50,verbose_name='Nombres')
    apellidos=models.CharField(max_length=50,verbose_name='Apellidos',null=True,blank=True)
    tipoPersonaId=models.ForeignKey(TipoPersona,on_delete=models.PROTECT,verbose_name='Tipo persona',null=True,blank=True)
    tipoDocumentoId=models.ForeignKey(TipoDocumento,on_delete=models.PROTECT,verbose_name='Tipo documento',null=True,blank=True)
    celular=models.CharField(max_length=15,verbose_name='Celular')
    correo=models.CharField(max_length=50,verbose_name='Correo electrónico',null=True,blank=True)
    departamentoId=models.ForeignKey(Departamentos,on_delete=models.PROTECT,null=True,blank=True)
    municipioId=models.ForeignKey(Municipios,on_delete=models.PROTECT,null=True,blank=True)
    direccion=models.CharField(max_length=50,verbose_name='Dirección')
    nombreContacto=models.CharField(max_length=50,verbose_name='Nombre contacto',null=True,blank=True)
    celularContacto=models.CharField(max_length=15,verbose_name='Celular contacto',null=True,blank=True)
    dateCreate=models.DateTimeField(auto_now=True,null=True,blank=True)
    dateUpdate=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.nombres
    
    class Meta:
        db_table="tblClientes"

