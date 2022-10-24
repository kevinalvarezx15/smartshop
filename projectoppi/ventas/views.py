from django.shortcuts import render
from datetime import date, datetime
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from compra.forms import CompraForm
from ventas.models import DetalleVenta
from ventas.forms import VentaForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
#from compra.models import Compra, DetalleCompra
from ventas.models import  Venta
from productos.models import Productos
from django.utils.dateparse import parse_date

class VentaListView(ListView):
    model=Venta
    template_name = 'ventas/listar.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Venta.objects.all():
                    data.append(i.toJSON())
                print(data)
            elif action == 'search_details_prod':
                print('ingresa')
                data = []
                for i in DetalleVenta.objects.filter(venta_id=request.POST['Venta_Id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ventas'
        context['titlepag'] = 'Ventas'
        return context

class VentaCreateView(CreateView):
    model: Venta
    form_class=VentaForm
    template_name= 'ventas/create.html'
    success_url=reverse_lazy('ventas:ventas')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Productos.objects.filter(nombre__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    venta = json.loads(request.POST['ventas'])
                    print(venta)
                    
                    ventas = Venta()
                    ventas.fechaVenta = datetime.now()
                    ventas.dateUpdate=datetime.now()
                    ventas.cliente_id =venta['cliente']
                    ventas.estadoVenta_id = venta['estadoVenta']
                    ventas.total = float(venta['total'])
                    ventas.save()
                    for i in venta['productos']:
                        prod=Productos()
                        prods = Productos.objects.filter(id=i['id'])
                        for k in prods:
                            prod.id=i['id']
                            prod.nombre=k.nombre
                            prod.descripcion=k.descripcion
                            prod.tipoProducto_id=k.tipoProducto_id
                            prod.cantidad=int(k.cantidad)-int(i['cantidad'])
                            prod.precio_venta=float(k.precio_venta)
                        prod.save()

                        det = DetalleVenta()
                        det.venta_id = ventas.Venta_Id
                        det.producto_id = i['id']
                        det.cantidad = int(i['cantidad'])
                        det.precioVenta = float(i['precio_venta'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['url'] = reverse_lazy('ventas:crearVenta')
        context['action'] = 'add'
        return context

# Create your views here.
