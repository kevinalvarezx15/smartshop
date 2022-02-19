from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    nombre=models.CharField(max_length=50,verbose_name='Nombres')
    descripcion=models.CharField(max_length=150,verbose_name='Descripcion')

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table="tblTipoProductos"

class Productos(models.Model):
    nombre=models.CharField(max_length=50,verbose_name='Nombre')
    descripcion=models.CharField(max_length=150,verbose_name='Descripcion')
    tipoProducto=models.ForeignKey(TipoProducto,on_delete=models.PROTECT,verbose_name='Tipo producto',null=True,blank=True)
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table="tblProductos"
