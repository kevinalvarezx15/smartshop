from django.db import models
from datetime import datetime
from proveedores.models import Proveedores
from productos.models import Productos
from cliente.models import Clientes
from django.forms import model_to_dict
# Create your models here.
class EstadoVenta(models.Model):
    estadoVenta_Id=models.AutoField(verbose_name='Estado Venta Id',primary_key=True)
    nombre=models.CharField(max_length=50,verbose_name='Nombre')
    descripcion=models.CharField(max_length=200,verbose_name='Descripcion')

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table="tblEstadoVenta"

class Venta(models.Model):
    Venta_Id=models.AutoField(verbose_name='Venta Id',primary_key=True)
    cliente=models.ForeignKey(Clientes,on_delete=models.PROTECT,null=True,blank=True)
    estadoVenta=models.ForeignKey(EstadoVenta,on_delete=models.PROTECT,null=True,blank=True)
    fechaVenta=models.DateField(null=True,blank=True,verbose_name='Fecha venta',default=datetime.now)
    dateUpdate=models.DateField(null=True,blank=True, verbose_name='Fecha actualización',default=datetime.now)   
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)


    def __str__(self):
        return self.proveedor.nombres
    
    def toJSON(self):
        item = model_to_dict(self)
        item['cliente'] = self.cliente.nombres
        item['estadoVenta'] = self.estadoVenta.nombre
        item['total'] = format(self.total, '.2f')
        item['fechaVenta'] = self.fechaVenta.strftime('%Y-%m-%d')
        return item
    
    class Meta:
        db_table="tblVentas"

class DetalleVenta(models.Model):
    detalleVenta=models.AutoField(verbose_name='Detalle venta Id',primary_key=True)
    venta=models.ForeignKey(Venta,on_delete=models.CASCADE,null=True,blank=True)
    producto=models.ForeignKey(Productos,on_delete=models.PROTECT,null=True,blank=True)
    cantidad=models.IntegerField(default=0,verbose_name='Cantidad')
    precioVenta=models.DecimalField(default=0.00,max_digits=9, decimal_places=2,verbose_name='Precio compra')    
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def toJSON(self):
        item = model_to_dict(self, exclude=['venta'])
        item['producto'] = self.producto.toJSON()
        item['precioVenta'] = format(self.precioVenta, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item
    
    class Meta:
        db_table="tblDetalleVenta"




