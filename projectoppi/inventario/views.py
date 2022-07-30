from gc import get_objects
from logging import exception
from urllib import request
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,DeleteView
from productos.forms import ProductoForm, TipoProductoForm
from django.utils.safestring import mark_safe
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from productos.models import Productos, TipoProducto


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class InventarioListView(ListView):
    model=Productos
    template_name='inventario/vista.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos'
        context['titlepag'] = 'Inventario'
        return context

