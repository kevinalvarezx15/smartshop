from django.shortcuts import render

# Create your views here.
def cargar_proveedores(request):   
   return render(
        request,
        'projecto/MostrarProveedores.html'
    )

def addnew(request):  
    
    return render(request,'projecto/CrearProveedor.html',) 