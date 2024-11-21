from django.urls import path 
from .views import*
from .views import login_view


urlpatterns = [

    path('', vista_home, name='home'),
    path('about/',vista_about),
    path('productos', vista_articulo, name='articulo'),
    path('contacto/',vista_contacto, name='contacto'),   
    path('lista_producto/',vista_lista_producto, name='lista_producto'),
    path('agregar_producto/',vista_agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:id_prod>/',vista_editar_producto, name='editar_producto'),
    path('ver_producto/<int:id_prod>/',vista_ver_producto, name='ver_producto'),
    path('eliminar_producto/<int:id_prod>/',vista_eliminar_producto, name='eliminar_producto'),
    path('login/', login_view, name='login'),
    
] 