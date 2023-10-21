from django.shortcuts import render, redirect
from .models import Regalo, Comentario, Invitado, Pareja, Avatar
from .forms import RegaloForm, ComentarioForm, InvitadoForm, ParejaForm, UserEditForm, UserRegisterForm,  IniciarSesionForm , AvatarForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, LogoutView
from django.views.generic import CreateView, TemplateView, UpdateView 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from AppCurso.context_processors import custom_user



#-------------------------------Regalos----------------------------------
@login_required
def lista_regalos(request):
    regalos = Regalo.objects.all()
    form = RegaloForm()

    if request.method == 'POST':
        form = RegaloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_regalos')  

    context = {"regalos": regalos, "form": form}
    return render(request, "AppCurso/lista_regalos.html", context)


@login_required
def agregar_regalo(request):
    if request.method == 'POST':
        form = RegaloForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('lista_regalos')  
    else:
        form = RegaloForm()
    return render(request, "AppCurso/agregar_regalo.html", {"form": form})

@login_required
def editar_regalo(request, regalo_id):
    regalo = Regalo.objects.get(pk=regalo_id)
    if request.method == 'POST':
        formulario = RegaloForm(request.POST, instance=regalo)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_regalos')
    else:
        formulario = RegaloForm(instance=regalo)
    return render(request, "AppCurso/editar_regalo.html", {"formulario": formulario, "regalo": regalo})

@login_required
def borrar_regalo(request, regalo_id):
    regalo = Regalo.objects.get(pk=regalo_id)
    if request.method == 'POST':
        regalo.delete()
        return redirect('lista_regalos')
    return render(request, "AppCurso/borrar_regalo.html", {"regalo": regalo})

#-------------------------------Comentarios----------------------------------
@login_required
def comentarios(request):
    comentarios = Comentario.objects.all()
    context = {"comentarios": comentarios}
    return render(request, "AppCurso/comentarios.html", context)

@login_required
def agregar_comentario(request):
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            comentario = formulario.save()
            return redirect('comentarios')
    else:
        formulario = ComentarioForm()
    return render(request, "AppCurso/agregar_comentario.html", {"formulario": formulario})

@login_required
def editar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(pk=comentario_id)
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST, instance=comentario)
        if formulario.is_valid():
            formulario.save()
            return redirect('comentarios')
    else:
        formulario = ComentarioForm(instance=comentario)
    return render(request, "AppCurso/editar_comentario.html", {"formulario": formulario, "comentario": comentario})

@login_required
def borrar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(pk=comentario_id)
    if request.method == 'POST':
        comentario.delete()
        return redirect('comentarios')
    return render(request, "AppCurso/borrar_comentario.html", {"comentario": comentario})


#-------------------------------Parejas----------------------------------
@login_required
def lista_parejas(request):
    parejas = Pareja.objects.all()
    context = {"parejas": parejas}
    return render(request, "AppCurso/lista_parejas.html", context)

@login_required
def agregar_pareja(request):
    if request.method == 'POST':
        form = ParejaForm(request.POST, request.FILES)  
        if form.is_valid():
            nueva_pareja = form.save(commit=False)
            nueva_pareja.foto = form.cleaned_data.get('foto')  
            nueva_pareja.save()
            return redirect('lista_parejas')
    else:
        form = ParejaForm()
    return render(request, "AppCurso/agregar_pareja.html", {"form": form})

@login_required
def editar_pareja(request, pareja_id):
    pareja = Pareja.objects.get(pk=pareja_id)
    if request.method == 'POST':
        formulario = ParejaForm(request.POST, instance=pareja)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_parejas')
    else:
        formulario = ParejaForm(instance=pareja)
    return render(request, "AppCurso/editar_pareja.html", {"formulario": formulario, "pareja": pareja})

@login_required
def borrar_pareja(request, pareja_id):
    pareja = Pareja.objects.get(pk=pareja_id)
    if request.method == 'POST':
        pareja.delete()
        return redirect('lista_parejas')
    return render(request, "AppCurso/borrar_pareja.html", {"pareja": pareja})


#-------------------------------Invitados----------------------------------
@login_required
def lista_invitados(request):
    invitados = Invitado.objects.all()
    context = {"invitados": invitados}
    return render(request, "AppCurso/lista_invitados.html", context)

@login_required
def agregar_invitado(request):
    if request.method == 'POST':
        formulario = InvitadoForm(request.POST)
        if formulario.is_valid():
            invitado = formulario.save()
            return redirect('lista_invitados')
    else:
        formulario = InvitadoForm()
    return render(request, "AppCurso/agregar_invitado.html", {"formulario": formulario})

@login_required
def editar_invitado(request, invitado_id):
    invitado = Invitado.objects.get(pk=invitado_id)
    if request.method == 'POST':
        formulario = InvitadoForm(request.POST, instance=invitado)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_invitados')
    else:
        formulario = InvitadoForm(instance=invitado)
    return render(request, "AppCurso/editar_invitado.html", {"formulario": formulario, "invitado": invitado})

@login_required
def borrar_invitado(request, invitado_id):
    invitado = Invitado.objects.get(pk=invitado_id)
    if request.method == 'POST':
        invitado.delete()
        return redirect('lista_invitados')
    return render(request, "AppCurso/borrar_invitado.html", {"invitado": invitado})


def inicio(request):
    context = custom_user(request)
    return render(request, 'AppCurso/inicio.html', context)



#-------------------Inicio - Registro - Sesion----------------------------------

class RegistroUsuarioView(CreateView):
    form_class = UserRegisterForm
    template_name = 'AppCurso/registro.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('editar_perfil')
        return super().get(request, *args, **kwargs)
    
class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'AppCurso/editar_perfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        # Guarda el formulario y la nueva contraseña
        user = form.save(commit=False)
        new_password = form.cleaned_data.get('new_password')
        
        if new_password:
            user.set_password(new_password)
            update_session_auth_hash(self.request, user)  # Actualiza la sesión con la nueva contraseña
        user.save()

        return super().form_valid(form)
    
# Vista de inicio de sesión 

class IniciarSesionView(LoginView):
    template_name = 'AppCurso/login.html'
    
    

# Vista de inicio

class InicioView(TemplateView):
    template_name = 'AppCurso/inicio.html'

# Vista de inicio de contraseña exitoso 
class CambioContrasenaExitosoView(TemplateView):
    template_name = 'AppCurso/cambio_contrasena_exitoso.html'
    
    
    
class CambiarContrasenaView(PasswordChangeView):
    template_name = 'AppCurso/cambiar_contrasena.html'  # Esto es para el cambio de contraseña
    success_url = reverse_lazy('cambio_contrasena_exitoso')  
    def form_valid(self, form):
        response = super().form_valid(form)
        # Cierra la sesión del usuario después de cambiar la contraseña
        logout(self.request)
        return response
    

#Cierre de sesion
class CustomLogoutView(View):
    template_name = 'AppCurso/logout.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect('login')  
        else:
            return redirect('login')
     
        
#--------------------------Acerca de mi--------------------------    
   
def acerca_de(request):
    return render(request, 'AppCurso/acercaDeMi.html')


#------------------Avatar------------------------
@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            avatar, created = Avatar.objects.get_or_create(user=user)

            if not created:
                avatar.imagen.delete()  # Borra la imagen anterior
                avatar.imagen = form.cleaned_data['imagen']
            else:
                avatar.imagen = form.cleaned_data['imagen']

            avatar.save()
            return redirect('inicio')  # Redirige a la página de inicio
    else:
        form = AvatarForm()
    return render(request, "AppCurso/agregar_avatar.html", {"form": form})
