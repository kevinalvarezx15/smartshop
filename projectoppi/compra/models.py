from datetime import datetime
from django.db import models
from proveedores.models import Proveedores
from productos.models import Productos
from django.forms import model_to_dict

# Create your models here.
class EstadoCompra(models.Model):
    estadoCompra_Id=models.IntegerField(verbose_name='Estado compra Id',primary_key=True)
    nombre=models.CharField(max_length=50,verbose_name='Nombre')
    descripcion=models.CharField(max_length=200,verbose_name='Descripcion')
    dateCreate=models.DateTimeField(auto_now=True,null=True,blank=True)
    dateUpdate=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table="tblEstadoCompra"

class Compra(models.Model):
    Compra_Id=models.AutoField(verbose_name='Compra Id',primary_key=True)
    proveedor=models.ForeignKey(Proveedores,on_delete=models.PROTECT,null=True,blank=True)
    estadoCompra=models.ForeignKey(EstadoCompra,on_delete=models.PROTECT,null=True,blank=True)
    fechaCompra=models.DateField(null=True,blank=True,verbose_name='Fecha compra',default=datetime.now)
    dateUpdate=models.DateField(null=True,blank=True, verbose_name='Fecha actualización',default=datetime.now)   
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)



    def toJSON(self):
        item = model_to_dict(self)
        item['proveedor'] = self.proveedor.nombres
        item['estadoCompra'] = self.estadoCompra.nombre
        item['total'] = format(self.total, '.2f')
        item['fechaCompra'] = self.fechaCompra.strftime('%Y-%m-%d')
        return item
    
    class Meta:
        db_table="tblCompras"

class DetalleCompra(models.Model):
    detalleCompra=models.AutoField(verbose_name='Detalle compra Id',primary_key=True)
    compra=models.ForeignKey(Compra,on_delete=models.CASCADE,null=True,blank=True)
    producto=models.ForeignKey(Productos,on_delete=models.PROTECT,null=True,blank=True)
    cantidad=models.IntegerField(default=0,verbose_name='Cantidad')
    precioCompra=models.DecimalField(default=0.00,max_digits=9, decimal_places=2,verbose_name='Precio compra')    
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def toJSON(self):
        item = model_to_dict(self, exclude=['compra'])
        item['producto'] = self.producto.toJSON()
        item['precioCompra'] = format(self.precioCompra, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item
    
    class Meta:
        db_table="tblDetalleCompra"