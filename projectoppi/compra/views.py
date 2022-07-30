from datetime import date, datetime
import json

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from compra.forms import CompraForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from compra.models import Compra, DetalleCompra
from productos.models import Productos
from django.utils.dateparse import parse_date

class CompraListView(ListView):
    model=Compra
    template_name = 'compra/list.html'

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
                for i in Compra.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                for i in DetalleCompra.objects.filter(compra_id=request.POST['Compra_Id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de compras'
        context['titlepag'] = 'Compras'
        return context

class CompraCreateView(CreateView):
    model: Compra
    form_class=CompraForm
    template_name= 'compra/create.html'
    success_url=reverse_lazy('compra:compra')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('prid')
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Productos.objects.filter(nombre__icontains=request.POST['term'])[0:10]
                print(prods)
                for i in prods:
                    print('prid')
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
                
            elif action == 'add':
                with transaction.atomic():
                    compras = json.loads(request.POST['compras'])
                    print(compras)
                    
                    compra = Compra()
                    compra.fechaCompra = compras['fechaCompra']
                    compra.dateUpdate=datetime.now()
                    compra.proveedor_id =compras['proveedor']
                    compra.estadoCompra_id = float(compras['estadoCompra'])
                    compra.total = float(compras['total'])
                    compra.save()
                    for i in compras['productos']:
                        prod=Productos()
                        prods = Productos.objects.filter(id=i['id'])
                        for k in prods:
                            prod.id=i['id']
                            prod.nombre=k.nombre
                            prod.descripcion=k.descripcion
                            prod.tipoProducto_id=k.tipoProducto_id
                            prod.cantidad=int(k.cantidad)+int(i['cantidad'])
                            prod.precio_venta=float(k.precio_venta)
                        prod.save()
                        
                        det = DetalleCompra()
                        det.compra_id = compra.Compra_Id
                        det.producto_id = i['id']
                        det.cantidad = int(i['cantidad'])
                        det.precioCompra = float(i['precio_compra'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            context['url'] = reverse_lazy('compra:crearCompra')
            context['action'] = 'add'
            return context

class CompraUpdateView(UpdateView):
    model: Compra
    form_class=CompraForm
    template_name= 'compra/create.html'
    success_url=reverse_lazy('compra:compra')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('prid')
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Productos.objects.filter(nombre__icontains=request.POST['term'])[0:10]
                for i in prods:
                    print('prid')
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            elif action == 'edit':
                with transaction.atomic():
                    compras = json.loads(request.POST['compras'])
                    print(compras)
                    
                    compra = Compra()
                    compra.fechaCompra = compras['fechaCompra']
                    compra.dateUpdate=datetime.now()
                    compra.proveedor_id =compras['proveedor']
                    compra.estadoCompra_id = float(compras['estadoCompra'])
                    compra.total = float(compras['total'])
                    compra.save()
                    for i in compras['productos']:
                        prod=Productos()
                        prods = Productos.objects.filter(id=i['id'])
                        for k in prods:
                            prod.id=i['id']
                            prod.nombre=k.nombre
                            prod.descripcion=k.descripcion
                            prod.tipoProducto_id=k.tipoProducto_id
                            prod.cantidad=int(k.cantidad)+int(i['cantidad'])
                            prod.precio_venta=float(k.precio_venta)
                        prod.save()
                        
                        det = DetalleCompra()
                        det.compra_id = compra.Compra_Id
                        det.producto_id = i['id']
                        det.cantidad = int(i['cantidad'])
                        det.precioCompra = float(i['precio_compra'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            context['url'] = reverse_lazy('compra:crearCompra')
            context['action'] = 'edit'
            return context

