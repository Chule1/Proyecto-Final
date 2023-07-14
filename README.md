# Proyecto Final Coronel

Alumno: Matías Ariel Coronel

Para ver esta entrega dirigirse a la rama "Final".

La aplicacion está orientada a la oferta y solicitud de clases particulares o tutorías de materias de las ciencias exactas e ingeniería.
Previo registri, permite al usuario publicar solicitud de clases (adjuntando el temario como imagen) o bien ofrecer como docente sus
clases particulares (adjuntando un flyer publicitario o imagen alusiva). 
A nivel de esta entrega se dejaron operativas dos materias (matemática y física). 
La primera de ellas mostrando toda la info de cada clase en el listado y la segunda a través de una lista reducida y botones Ver Mas
para pasar al detalle de cada clase publicada.
Para la comunicación entre usuarios se habilitaron comentarios en cada clase detallada (solo en física), que permiten incluso a usuarios
no registrados dejar consultas exponiendo nombre y mensaje.

Las URL disponibles son las siguientes:

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
    path('Alumnos/',Alumnos,name="Alumnos"),
    path('AboutUs/',AboutUs,name="AboutUs"),
    path('Proximamente/',Proximamente,name="Proximamente"),
    path('Clases/',Clase,name="Clases"),
    path('CrearClase/',CrearClase,name="CrearClase"),
    path('EditarClase/<id_clase>', EditarClase, name="EditarClase"),
    path('BorrarClase/<id_clase>', BorrarClase, name="BorrarClase"),
    path('DetalleClase/<int:clase_id>/', DetalleClase, name='DetalleClase'),
    path('listaMatematica/',listaMatematica,name="listaMatematica"),
    path('listaFisica/',listaFisica,name="listaFisica"),
    path('DetalleClase/<int:clase_id>/comentario/', ComentarioPagina.as_view(), name='comentario')


Se dejo precargado el usuario:
UsuarioPrueba1
pass: prueba123

Si quisieran ver algo desde el admin deje creado un superusuario para los tutores del curso que se los dejo en la entrega en CODER.
El video de presentación de la entrega es: https://youtu.be/son85c7QvD8

