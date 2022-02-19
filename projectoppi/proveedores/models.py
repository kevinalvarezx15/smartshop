from django.db import models
from cliente.models import Paises, TipoDocumento, Departamentos, Municipios

# Create your models here.
class Proveedores(models.Model):
    documento=models.BigIntegerField(verbose_name='Número documento',primary_key=True)
    nombres=models.CharField(max_length=50,verbose_name='Nombres')
    tipoDocumentoId=models.ForeignKey(TipoDocumento,on_delete=models.PROTECT,verbose_name='Tipo documento',null=True,blank=True)
    celular=models.CharField(max_length=15,verbose_name='Celular')
    correo=models.CharField(max_length=50,verbose_name='Correo electrónico',null=True,blank=True)
    pais=models.ForeignKey(Paises,on_delete=models.PROTECT,null=True,blank=True)
    departamentoId=models.ForeignKey(Departamentos,on_delete=models.PROTECT,null=True,blank=True)
    municipioId=models.ForeignKey(Municipios,on_delete=models.PROTECT,null=True,blank=True)
    direccion=models.CharField(max_length=50,verbose_name='Dirección')
    dateCreate=models.DateTimeField(auto_now=True,null=True,blank=True)
    dateUpdate=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.nombres
    
    class Meta:
        db_table="tblProveedores"

