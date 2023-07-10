from django.urls import path
from App1.views import * 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio,name="inicio"),
    path('Empty/', Empty, name="Empty"),
    path('login/', loginWeb, name="login"),
    path('registro/', registro, name="registro"),
    path('Perfil/', perfilview, name="Perfil"),
    path('Logout/',LogoutView.as_view(template_name = 'login.html'), name="Logout"),
    path('Perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('Perfil/changePassword/', changePassword, name="changePassword"),
    path('Perfil/changeAvatar/', editAvatar, name="editAvatar"),
    path('Tutores/',Tutores,name="Tutores"),
    path('Clases/',Clase,name="Clases"),
    path('CrearClase/',CrearClase,name="CrearClase"),
    path('EditarClase/<id_clase>', EditarClase, name="EditarClase"),
    path('BorrarClase/<id_clase>', BorrarClase, name="BorrarClase"),
    path('DetalleClase/<int:clase_id>/', DetalleClase, name='DetalleClase'),

    path('listaMatematica/',listaMatematica,name="listaMatematica"),
    path('listaFisica/',listaFisica,name="listaFisica"),

    path('DetalleClase/<int:clase_id>/comentario/', ComentarioPagina.as_view(), name='comentario')
]
