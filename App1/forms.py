import datetime
from django import forms
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from App1.models import *

MateriaSeleccion = (
    ('matemática','Matemática'),
    ('física', 'Física'),
    ('química','Química'),
    ('especialidad','Especialidad'))

TipoSeleccion = ( ('se ofrece','Se Ofrece'),
    ('se necesita', 'Se Necesita'),)

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Last Name"}))
    #password = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder":"Password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] #'password'
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Old password"}))
    new_password1 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"New password"}))
    new_password2 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Confirmation new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar = forms.ImageField()

class FormNuevaClase(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
    titulo = forms.CharField(max_length=200)
    tipo = forms.ChoiceField(choices=TipoSeleccion, initial='se ofrece')
    materia = forms.ChoiceField(choices=MateriaSeleccion, initial='matemática')
    nivel = forms.CharField(max_length=20)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    fechaPublicacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=datetime.date.today)
    telefonoContacto = forms.IntegerField()
    emailContacto = forms.EmailField()
    imagenAlusiva = forms.ImageField(required=False)

    class Meta:
        model = Clases
        fields = '__all__'


class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),}
