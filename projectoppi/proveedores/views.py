from re import template
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,DeleteView
from proveedores.models import Proveedores
from proveedores.forms import ProveedoresForm
from cliente.models import Departamentos,Paises,TipoDocumento,Municipios

# Create your views here.
class ProvedoresListView(ListView):
    model=Proveedores
    template_name='proveedores/MostrarProveedor.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de proveedores'
        context['titlepag'] = 'Proveedores'
        return context
class ProveedorCreateView(CreateView):
    try:
        model=Proveedores
        form_class=ProveedoresForm
        template_name='proveedores/CrearProveedor.html'
        success_url=reverse_lazy('proveedores:proveedores')

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
            context['url'] = reverse_lazy('proveedores:crearProveedor')
            print("hello")
            return context
    except Exception as ex:
        print(ex)

class ProveedoresUpdateView(UpdateView):
    model=Proveedores
    form_class=ProveedoresForm
    template_name='proveedores/CrearProveedor.html'
    success_url=reverse_lazy('proveedores:proveedores')

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
        context['url'] = reverse_lazy('proveedores:EditarProveedor',kwargs={'pk': idcon})
        context['idcom'] =  "object.pk"
        context['mode']="edit"
        return context

    
def selectProveedores(request):

    data={}
    try:
        action=request.POST['action']
        if action=='search_tipoDepartamento_id':
            print(request.POST['id'])
            data=[{'id':'', 'text':'---------'}]
            for i in Departamentos.objects.filter(pais=request.POST['id']):
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

class ProveedorDeleteView(DeleteView):
    model=Proveedores
    #template_name='cliente/EliminarCliente.html'
    success_url=reverse_lazy('proveedores:proveedores')

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


def cargar_proveedores(request):   
   return render(
        request,
        'projecto/MostrarProveedores.html'
    )

def addnew(request):  
    
    return render(request,'projecto/CrearProveedor.html',) 