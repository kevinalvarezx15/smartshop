from ast import pattern
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.views import LogoutView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.views.generic import RedirectView

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
        User = get_user_model()
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