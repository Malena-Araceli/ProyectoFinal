from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import RegistroUsuarioView, EditarPerfilView, CambioContrasenaExitosoView, IniciarSesionView, CambiarContrasenaView
from django.contrib.auth.views import LogoutView

urlpatterns = [
 path('',views.inicio,name='inicio'),
 path('lista_regalos/', views.lista_regalos, name='lista_regalos'),
 path('agregar_regalo/', views.agregar_regalo, name='agregar_regalo'),
 path('agregar_pareja/', views.agregar_pareja, name='agregar_pareja'),
 path('lista_parejas/', views.lista_parejas, name='lista_parejas'),
 path('editar_pareja/<int:pareja_id>/', views.editar_pareja, name='editar_pareja'),
 path('borrar_pareja/<int:pareja_id>/', views.borrar_pareja, name='borrar_pareja'),
 path('regalos/editar/<int:regalo_id>/', views.editar_regalo, name='editar_regalo'),
 path('regalos/borrar/<int:regalo_id>/', views.borrar_regalo, name='borrar_regalo'),
 path('comentarios/', views.comentarios, name='comentarios'),
 path('agregar_comentario/', views.agregar_comentario, name='agregar_comentario'),
 path('editar_comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
 path('borrar_comentario/<int:comentario_id>/', views.borrar_comentario, name='borrar_comentario'),
 path('lista_invitados/', views.lista_invitados, name='lista_invitados'),
 path('agregar_invitado/', views.agregar_invitado, name='agregar_invitado'),
 path('editar_invitado/<int:invitado_id>/', views.editar_invitado, name='editar_invitado'),
 path('borrar_invitado/<int:invitado_id>/', views.borrar_invitado, name='borrar_invitado'),

    
         #---------------Inicio sesion, cierre y registro-----------------------
    path('registro/', views.RegistroUsuarioView.as_view(), name='registro'),
    path('perfil/editar/', views.EditarPerfilView.as_view(), name='editar_perfil'),
    path('contrasena/cambiar/', views.CambiarContrasenaView.as_view(), name='cambiar_contrasena'),
    path('contrasena/cambio_exitoso/', views.CambioContrasenaExitosoView.as_view(), name='cambio_contrasena_exitoso'),
    path('login/', views.IniciarSesionView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
    #------------Acerca de Mi---------------
    path('acercaDeMi/', views.acerca_de, name='acercaDeMi'),
    
    #--------------avatar--------------
    path('agregar_avatar/', views.agregar_avatar, name='agregar_avatar'),
    


]





