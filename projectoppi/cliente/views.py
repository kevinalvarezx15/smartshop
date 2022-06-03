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



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
# Create your views here.
def cargar_cliente(request):   
   return render(
        request,
        'cliente/show.html'
    )

class ClienteListView(ListView):
    model=Clientes
    template_name='cliente/show.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['titlepag'] = 'Clientes'
        return context

class ClientesCreateView(CreateView):
    try:
        model=Clientes
        form_class=ClienteForm
        template_name='cliente/CrearCliente.html'
        success_url=reverse_lazy('cliente:cliente')
        
        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            return super().dispatch(request, *args, **kwargs)

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
            context['url'] = reverse_lazy('cliente:crearCliente')
            print("hello")
            return context
    except Exception as ex:
        print(ex)
    

def selectCliente(request):

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

class ClienteUpdateView(UpdateView):
    model=Clientes
    form_class=ClienteForm
    template_name='cliente/CrearCliente.html'
    success_url=reverse_lazy('cliente:cliente')


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
        context['url'] = reverse_lazy('cliente:EditarCliente',kwargs={'pk': idcon})
        context['mode']="edit"
        context['idcom'] =  "object.pk"
        return context

class ClienteDeleteView(DeleteView):
    model=Clientes
    #template_name='cliente/EliminarCliente.html'
    success_url=reverse_lazy('cliente:cliente')

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

def addnew(request):  
    
    return render(request,'cliente/CrearCliente.html',) 

def editCliente(request,id):  
    #if request.method=='GET':
        
    return render(request,'projecto/CrearCliente.html',{'id':id}) 
    

