from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,DeleteView
from productos.forms import ProductoForm, TipoProductoForm
from productos.models import Productos, TipoProducto

# Create your views here.
class TipoProductoListView(ListView):
    model=TipoProducto
    template_name='tipoproducto/mostrartipoproducto.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tipo Productos'
        context['titlepag'] = 'Tipo Productos'
        return context

class TipoProductoCreateView(CreateView):
    try:
        model=TipoProducto
        form_class=TipoProductoForm
        template_name='tipoproducto/creartipoproducto.html'
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
            context['url'] = reverse_lazy('tipoproductos:crearTipoproducto')
            print("hello")
            return context
    except Exception as ex:
        print(ex)
     
class TipoProductoUpdateView(UpdateView):
    model=TipoProducto
    form_class=TipoProductoForm
    template_name='tipoproducto/creartipoproducto.html'
    success_url=reverse_lazy('tipoproductos:tipoproducto')

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
        context['url'] = reverse_lazy('tipoproductos:EditarTipoproducto',kwargs={'pk': idcon})
        context['idcom'] =  "object.pk"
        return context

class TipoProductoDeleteView(DeleteView):
    model=TipoProducto
    #template_name='cliente/EliminarCliente.html'
    success_url=reverse_lazy('tipoproductos:tipoproducto')

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

