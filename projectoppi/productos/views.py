from django.shortcuts import render

# Create your views here.
def cargar_productos(request):   
   return render(
        request,
        'projecto/MostrarProductos.html'
    )

def addnew(request):  
    
    return render(request,'projecto/CrearProducto.html',) 

def cargar_TipoProducto(request):   
   return render(
        request,
        'projecto/MostrarTipoProducto.html'
    )

def addnewTipoProducto(request):   
   return render(
        request,
        'projecto/CrearTipoProducto.html'
    )
