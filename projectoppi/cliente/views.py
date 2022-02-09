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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        return context

class ClientesCreateView(CreateView):
    try:
        model=Clientes
        form_class=ClienteForm
        template_name='cliente/CrearCliente.html'
        success_url=reverse_lazy('cliente:cliente')

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

        # def post(self,request,*args,**kwargs):
            
        #     if is_ajax(request=request):
        #         form=self.form_class(request.POST)
        #         print("tipo")
        #         print(request.POST['tipoDocumentoId'])
        #         if form.is_valid():
                    
        #             nuevoCliente=Clientes(
        #                 documento=form.cleaned_data.get('documento'),
        #                 nombres=form.cleaned_data.get('nombres'),
        #                 apellidos=form.cleaned_data.get('apellidos'),
        #                 tipoPersonaId=form.cleaned_data.get('tipoPersonaId'),
        #                 tipoDocumentoId=form.cleaned_data.get('tipoDocumentoId'),                    
        #                 celular=form.cleaned_data.get('celular'),
        #                 correo=form.cleaned_data.get('correo'),
        #                 departamentoId=form.cleaned_data.get('departamentoId'),
        #                 municipioId=form.cleaned_data.get('municipioId'),
        #                 direccion=form.cleaned_data.get('direccion'),
        #                 nombreContacto=form.cleaned_data.get('nombreContacto'),
        #                 celularContacto=form.cleaned_data.get('celularContacto'),
        #                 dateCreate=form.cleaned_data.get('dateCreate'),
        #                 dateUpdate=form.cleaned_data.get('dateUpdate'),
        #             )
        #             print(nuevoCliente.tipoDocumentoId)
        #             #nuevoCliente.save()
        #             mensaje="Registro correctamente"
        #             error='No hay error'
        #             response=JsonResponse({'mensaje':mensaje,'error':error})
        #             response.status_code=201
        #             return response
        #         else:
        #             mensaje="No se ha podido registrar"
        #             error=form.errors
        #             response=JsonResponse({'mensaje':mensaje,'error':error})
        #             response.status_code=400
        #             return response
        #     else:
        #         return redirect('cliente:cliente')

        

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
            for i in TipoDocumento.objects.filter(TipoPersonaId=request.POST['id']):
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

    def post(self,request,*args,**kwargs):
        data={}
        try:
            print("Update")
            form=ClienteForm(request.POST)
            # if form.is_valid():
            form.save()
            # else:
            #     data['error']=form.errors
            
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        idcon=self.kwargs.get('pk')
        context['url'] = reverse_lazy('cliente:EditarCliente',kwargs={'pk': idcon})
        context['idcom'] =  "object.pk"
        return context

class ClienteDeleteView(DeleteView):
    model=Clientes
    template_name='cliente/EliminarCliente.html'
    success_url=reverse_lazy('cliente:cliente')

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
    

