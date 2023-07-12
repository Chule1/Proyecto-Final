from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from App1.models import *
from App1.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    avatar = getavatar(request)
    return render(request, "inicio.html",{"avatar": avatar})

def Empty(request):
    avatar = getavatar(request)
    return render(request, "Empty.html",{"avatar": avatar})

def Tutores(request):
    avatar = getavatar(request)
    return render(request, "Tutores.html",{"avatar": avatar})

def Alumnos(request):
    avatar = getavatar(request)
    return render(request, "Alumnos.html",{"avatar": avatar})

def AboutUs(request):
    avatar = getavatar(request)
    return render(request, "AboutUs.html",{"avatar": avatar})

def Clase(request):
    avatar = getavatar(request)
    return render(request, "AboutUs.html",{"avatar": avatar})

@login_required
def CrearClase(request):
    avatar = getavatar(request)
    return render(request, "CrearClase.html",{"avatar": avatar})

def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("../inicio")
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')

def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request, 'login.html')
    else:
        return render(request, 'registro.html')
    
@login_required  
def perfilview(request):
    avatar = getavatar(request)
    return render(request, 'Perfil.html',{"avatar": avatar})

@login_required  
def editarPerfil(request):
    avatar = getavatar(request)
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'Perfil.html',{"avatar": avatar})
    else:
        form = UserEditForm(initial= {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
        return render(request, 'editarPerfil.html', {"form": form,"avatar":avatar})

@login_required
def changePassword(request):
    usuario = request.user    
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
                return HttpResponse("Contraseña cambiada exitosamente")
            else:
                return HttpResponse("Las contraseñas no coinciden")
    else:
        form = ChangePasswordForm(user=usuario)
    
    return render(request, 'changePassword.html', {"form": form})

@login_required
def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "inicio.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "avatar.html", {'form': form})


def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar

#Listado de clases por materia.

def listaMatematica(request):
    avatar = getavatar(request)
    clases_matematica = Clases.objects.filter(materia='matemática')
    context = {'clases_matematica': clases_matematica, 'avatar': avatar}
    return render(request, 'listaMatematica.html', context)

def listaFisica(request):
    avatar = getavatar(request)
    clases_fisica = Clases.objects.filter(materia='física')
    context = {'clases_fisica': clases_fisica, 'avatar': avatar}
    return render(request, 'listaFisica.html', context)


#Crear una clase nueva
@login_required
def CrearClase(request):
    avatar = getavatar(request)
    ind_clase = Clases.objects.all()
    if request.method =='POST':
        ind_clase = Clases(usuario=request.user,titulo=request.POST["titulo"], tipo = request.POST["tipo"], materia = request.POST["materia"], nivel = request.POST["nivel"], descripcion = request.POST["descripcion"], fechaPublicacion = request.POST["fechaPublicacion"], telefonoContacto = request.POST["telefonoContacto"], emailContacto = request.POST["emailContacto"], imagenAlusiva = request.POST["imagenAlusiva"])
        ind_clase.save()
        miFormulario = FormNuevaClase()
        return render(request, "CrearClase.html",{"miFormulario":miFormulario, "ind_clase":ind_clase,"avatar":avatar})
    else:
        miFormulario = FormNuevaClase()
    return render(request, "CrearClase.html",{"miFormulario":miFormulario, "ind_clase":ind_clase,"avatar":avatar})    

    
#Edición y borrado de clases ofrecidas/pedidas.
def EditarClase(request, id_clase):
    avatar = getavatar(request)
    clase = Clases.objects.get(id=id_clase)
    if request.method == 'POST':
        miFormulario = FormNuevaClase(request.POST, request.FILES, instance=clase)
        if miFormulario.is_valid():
            if 'imagenAlusiva' in request.FILES:
                clase.imagenAlusiva = request.FILES['imagenAlusiva']
            miFormulario.save()
            clase.save()  # Guardar la instancia de la clase después de asignar la imagen
            miFormulario = FormNuevaClase(instance=clase)
            Clase = Clases.objects.all()
            return render(request, "CrearClase.html", {"miFormulario": miFormulario, "Clase": Clase, "avatar": avatar})
    else:
        miFormulario = FormNuevaClase(instance=clase)
    return render(request, "EditarClase.html", {"miFormulario": miFormulario, "avatar": avatar})


def BorrarClase(request,id_clase):
    clase = get_object_or_404(Clases, id=id_clase)
    if request.method == 'POST':
        clase.delete()
        return redirect('listaMatematica')
    return render(request, 'BorrarClase.html', {'clase': clase})

#Detalle de Clase
def DetalleClase(request, clase_id):
    avatar = getavatar(request)
    clase = get_object_or_404(Clases, pk=clase_id)
    comentarios = Comentario.objects.filter(comentario=clase)
    context = {'clase': clase, 'comentarios': comentarios, 'avatar': avatar}
    return render(request, 'detalleClase.html', context)


class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        clase = get_object_or_404(Clases, pk=self.kwargs['clase_id'])
        form.instance.comentario = clase
        return super().form_valid(form)
