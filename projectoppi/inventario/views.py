from gc import get_objects
from logging import exception
from urllib import request
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,DeleteView
from cliente.forms import ClienteForm
from cliente.models import Clientes, TipoDocumento,Municipios
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required



from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt,csrf_protect

class cargar_inventario(ListView):
    model=Clientes
    template_name='inventario/vista.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


