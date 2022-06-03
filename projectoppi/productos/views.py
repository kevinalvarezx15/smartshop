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
# Create your views here.


class ProductoListView(ListView):
    model=Productos
    template_name='productos/mostrarProducto.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos'
        context['titlepag'] = 'Productos'
        return context

class ProductoCreateView(CreateView):
    try:
        model=Productos
        form_class=ProductoForm
        template_name='productos/CrearProducto.html'
        success_url=reverse_lazy('productos:producto')


        def post(self,request,*args,**kwargs):
            data={}
            try:

                form=self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error']=form.errors
                
            except Exception as e:
                data['error']=str(e)
            return JsonResponse(data)


        def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            context['url'] = reverse_lazy('productos:crearProducto')
            print("hello")
            return context
    except Exception as ex:
        print(ex)
            
class ProductoUpdateView(UpdateView):
    model=Productos
    form_class=ProductoForm
    template_name='productos/CrearProducto.html'
    success_url=reverse_lazy('productos:producto')

    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        data={}
        try:
            print("Update")
            form=self.get_form()
            if form.is_valid():
                form.save()
            else:
                data['error']=form.errors
            
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        idcon=self.kwargs.get('pk')
        context['url'] = reverse_lazy('productos:EditarProducto',kwargs={'pk': idcon})
        context['idcom'] =  "object.pk"
        return context

class ProductoDeleteView(DeleteView):
    model=Productos
    #template_name='cliente/EliminarCliente.html'
    success_url=reverse_lazy('productos:producto')

    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        data={}
        try:
            self.object.delete()

        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        idcon=self.kwargs.get('pk')
        #context['url'] = reverse_lazy('cliente:EditarCliente',kwargs={'pk': idcon})
        #context['idcom'] =  "object.pk"
        return context


