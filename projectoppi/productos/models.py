from django.db import models
from django.forms import model_to_dict

# Create your models here.
class TipoProducto(models.Model):
    nombre=models.CharField(max_length=50,verbose_name='Nombres')
    descripcion=models.CharField(max_length=150,verbose_name='Descripcion')

    def __str__(self) -> str:
        return self.nombre
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    
    class Meta:
        db_table="tblTipoProductos"

class Productos(models.Model):
    nombre=models.CharField(max_length=50,verbose_name='Nombre')
    descripcion=models.CharField(max_length=150,verbose_name='Descripcion')
    tipoProducto=models.ForeignKey(TipoProducto,on_delete=models.PROTECT,verbose_name='Tipo producto',null=True,blank=True)
    cantidad=models.IntegerField(default=0,null=True,blank=True,verbose_name='Cantidad')
    precio_venta=models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    def __str__(self) -> str:
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['tipoProducto'] = self.tipoProducto.toJSON()
        return item
    
    class Meta:
        db_table="tblProductos"
