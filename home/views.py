from django.shortcuts import render, redirect
from .forms import *
from .models import Producto
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def vista_lista_producto (request):
    lista = Producto.objects.filter()
    return render(request, 'lista_producto.html',locals())

def vista_about(request):
    return render(request,'about.html')

def vista_articulo(request):
    return render(request,'articulo.html')

def vista_contacto(request):
    info_enviado=False
    email =""
    title =""
    text =""
    if request.method =="POSTt":
        formulario =contacto_form(request.POST)
        if formulario.is_valid():
            info_enviado=True
            email = formulario.cleamed_data['correo']
            title = formulario.cleamed_data['titulo']
            text = formulario.cleaned_data['texto']
    else: #si es metodo GET u otro metodo
        formulario= contacto_form()    
    return render(request,'contacto.html',locals())

def vista_home(request):
    return render(request, 'home.html')


# ----------- Agregar Producto -----------
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def vista_agregar_producto(request):
    
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('/lista_producto/')
    else:
        formulario = agregar_producto_form()
    return render(request, 'agregar_producto.html', locals() ) 

# ----------- Editar Producto -----------

def vista_editar_producto(request, id_prod):
    producto = Producto.objects.get(id = id_prod) #Consultar 1 producto por medio del id
    # SELECT * FROM producto WHERE id = id_prod 
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect ('/lista_producto/')
    else:
        formulario = agregar_producto_form(instance = producto)
    return render(request, 'agregar_producto.html', locals() ) 

# ----------- Ver Producto -----------

def vista_ver_producto(request, id_prod):
    producto = Producto.objects.get(id = id_prod) #Consultar 1 producto por medio del id
    # SELECT * FROM producto WHERE id = id_prod 
    return render(request, 'ver_producto.html', locals() ) 

# ----------- Eliminar Producto -----------

def vista_eliminar_producto(request, id_prod):
    producto = Producto.objects.get(id = id_prod) #Consultar 1 producto por medio del id
    
    producto.delete()
    # delete(producto)
    return redirect('/lista_producto/')
    return render(request, 'ver_producto.html', locals() ) 

# ----------- LOGINNN -----------

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
        print(request.user)
    return render(request, 'login.html', {'form': form})