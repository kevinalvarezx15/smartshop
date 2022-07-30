from argparse import Action
from ast import pattern
from audioop import reverse
from multiprocessing import context
from pyexpat import model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.urls import reverse_lazy



def cargar_login(request):
    if request.user.is_authenticated:
        return redirect('cliente:cliente')

    if request.method=='POST':
        print ('*')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('cliente:cliente')
        else:
            return render(request, 'projecto/login.html',{'error': 'Nombre de usuario o contraseña incorrecta'})
    return render(
        request,
        'projecto/login.html',
        {}
    )

def cargar_registro(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=User.objects.create_user(username=username,password=password)
        except IntegrityError:
            return render(request, 'projecto/registro.html',{'error': 'Nombre de usuario ya existe'})
        user.first_name=request.POST['nombre']
        user.last_name=request.POST['apellido']
        user.email=request.POST['email']
        user.save()

        return redirect('login')
    return render(
        request,
        'projecto/registro.html'
    )



def reset_passw(request):   
   return render(
        request,
        'projecto/resetpassword.html'
    )

class LogoutRedirectView(RedirectView):
    pattern_name='login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class UserChangePasswordView(LoginRequiredMixin, FormView ):
    model = User
    form_class = PasswordChangeForm
    template_name = 'projecto/changepassword.html'
    success_url = reverse_lazy('login')

    #@method_decorador(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        data ={}
        try:
            action = request.POST['action']
            if action == 'edit':
                form= PasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error']= 'No ha ingreso ninguna opción'
        except Exception as e:
            data['error'] =str(e)
        return JsonResponse(data)
    

    def get_context_data(self, **kwargs):
        context['title'] ='Edicion de Password'
        context['entity'] ='Password'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

        
