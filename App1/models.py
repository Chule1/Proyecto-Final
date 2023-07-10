from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #SubCarpeta de avatares
    image = models.ImageField(upload_to='avatares', null = True, blank = True)

class Clases(models.Model):
    MateriaSeleccion = (
    ('matemática','Matemática'),
    ('física', 'Física'),
    ('química','Química'),
    ('especialidad','Especialidad'))

    TipoSeleccion = ( ('se ofrece','Se Ofrece'),
    ('se necesita', 'Se Necesita'),)
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    tipo=models.CharField(max_length=15, choices=TipoSeleccion, default='se ofrece')
    materia= models.CharField(max_length=15, choices=MateriaSeleccion, default='matemática')
    nivel=models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenAlusiva = models.ImageField(null=True, blank=True, upload_to='imagenes')

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return f"{self.titulo} - {self.tipo} - Creada por: {self.usuario}"

class Comentario(models.Model):
    comentario = models.ForeignKey(Clases, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
