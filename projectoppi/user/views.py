from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from user.models import User
from user.forms import UserForm


# Create your views here.
class UserListView(LoginRequiredMixin,ListView):
    model = User
    template_name = 'user/list.html'
    permission_required = 'user.view_user'
    data = []


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'
        context['titlepag'] = 'Usuarios'
        return context

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model=User
    form_class=UserForm
    template_name='user/EditUser.html'
    success_url=reverse_lazy('user:user_list')

    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        data={}
        print('1')
        u = User.objects.get(username=request.POST['username'])
        print('2')
        u.first_name=request.POST['first_name']
        print(u.first_name)
        u.last_name=request.POST['last_name']
        u.email=request.POST['email']
        u.save()
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        idcon=self.kwargs.get('pk')
        context['url'] = reverse_lazy('user:EditarUser',kwargs={'pk': idcon})
        context['mode']="edit"
        context['idcom'] =  "object.pk"
        return context

class UserCreateView(CreateView):
    try:
        model=User
        form_class=UserForm
        template_name='user/EditUser.html'
        success_url=reverse_lazy('user:user_list')


        def post(self,request,*args,**kwargs):
            data={}
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            try:
                user=User.objects.create_user(username=username,password=password)
            except Exception as e:
                return render(request, 'projecto/registro.html',{'error': 'Nombre de usuario ya existe'})
            user.first_name=request.POST['first_name']
            user.last_name=request.POST['last_name']
            user.email=request.POST['email']
            user.save()
            return JsonResponse(data)

            


        def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            context['url'] = reverse_lazy('user:crearUser')
            print("hello")
            return context
    except Exception as ex:
        print(ex)

class UserDeleteView(DeleteView):
    model=User
    #template_name='cliente/EliminarCliente.html'
    success_url=reverse_lazy('user:user_list')

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
