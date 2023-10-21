from django import forms
from .models import Invitado, Pareja, Regalo, Comentario, Avatar
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User


class InvitadoForm(forms.ModelForm):
    class Meta:
        model = Invitado
        fields = ['nombre', 'apellido', 'email']




class ParejaForm(forms.ModelForm):
    fecha_casamiento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'])
    
    class Meta:
        model = Pareja
        fields = ['nombre_novio', 'nombre_novia', 'fecha_casamiento', 'foto']  



class RegaloForm(forms.ModelForm):
    class Meta:
        model = Regalo
        fields = ['nombre', 'descripcion', 'pareja', 'entregado']

        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'mensaje', 'pareja']
        
        
        
# Formulario de registro de usuario 
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

#Formulario para editar usuarios

class UserEditForm(UserChangeForm):
    new_password = forms.CharField(
        label='Nueva contraseña',
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Deja en blanco para mantener la contraseña actual'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['new_password'].help_text = 'Deja en blanco para mantener la contraseña actual'

    def clean_new_password(self):
        new_password = self.cleaned_data['new_password']
        if new_password:
            #para la nueva contraseña 
            if len(new_password) < 8:
                raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres')
        return new_password


# Formulario de inicio de sesión 
class IniciarSesionForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('imagen',)