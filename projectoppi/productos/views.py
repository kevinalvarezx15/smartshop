from gc import get_objects
from logging import exception
from urllib import request
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,DeleteView
from productos.forms import TipoProductoForm
from django.utils.safestring import mark_safe
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from productos.models import TipoProducto



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
# Create your views here.

def cargar_tipoproducto(request):   
   return render(
        request,
        'productos/mostrartipoproducto.html'
    )

class TipoProductoListView(ListView):
    model=TipoProducto
    template_name='productos/mostrartipoproducto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tipo Productos'
        context['titlepag'] = 'Tipo Productos'
        return context

class TipoProductoCreateView(CreateView):
    try:
        model=TipoProducto
        form_class=TipoProductoForm
        template_name='productos/creartipoproducto.html'
        success_url=reverse_lazy('productos:tipoproducto')

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
            context['url'] = reverse_lazy('productos:crearcrearTipoproducto')
            print("hello")
            return context
    except Exception as ex:
        print(ex)
    

    model=TipoProducto
    #template_name='cliente/EliminarCliente.html'
    success_url=reverse_lazy('productos:tipoproductos')

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

def selectTipoproducto(request):

    data={}
    try:
        action=request.POST['action']
        if action=='search_tipoDocumento_id':
            print(request.POST['id'])
            data=[{'id':'', 'text':'---------'}]
            for i in TipoDocumento.objects.filter(TipoPersonaId=1):
                data.append({'id':i.id,'text':i.nombre})
        elif action=='search_tipoMunicipio_id':
            print(request.POST['id'])
            data=[{'id':'', 'text':'---------'}]
            for i in Municipios.objects.filter(DepartamentoId=request.POST['id']):
                data.append({'id':i.id,'text':i.nombre})
        else:
            data['error']='Ha ocurrido un error'
            print("qqq")
    except Exception as ex:
        data['error']=str(ex)
    return JsonResponse(data,safe=False)
  
class TipoProductoUpdateView(UpdateView):
    model=TipoProducto
    form_class=TipoProductoForm
    template_name='productos/creartipoproducto.html'
    success_url=reverse_lazy('productos:tipoproductos')

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
        context['url'] = reverse_lazy('productos:EditarTipoproducto',kwargs={'pk': idcon})
        context['idcom'] =  "object.pk"
        return context

class TipoProductoDeleteView(DeleteView):
    model=TipoProducto
    #template_name='cliente/EliminarCliente.html'
    success_url=reverse_lazy('productos:tipoproducto')

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

