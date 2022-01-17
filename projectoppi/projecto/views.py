from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def cargar_login(request):
    if request.method=='POST':
        print ('*')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('cliente')
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
