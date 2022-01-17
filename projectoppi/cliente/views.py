from django.shortcuts import render,redirect


# Create your views here.
def cargar_cliente(request):   
   return render(
        request,
        'projecto/show.html'
    )

def addnew(request):  
    
    return render(request,'projecto/CrearCliente.html',) 

def editCliente(request,id):  
    #if request.method=='GET':
        
    return render(request,'projecto/CrearCliente.html',{'id':id}) 
    

