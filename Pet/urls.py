"""
URL configuration for Pet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pet.views import Principal,Contacto
from Pet.views import Elegir,RegistroLogin,IngresarLogin,Logout,ActualizarUsuario,EliminarUsuario


urlpatterns = [
    path('admin/', admin.site.urls),

    #Inicio
    path('Elegir/entrar',Elegir),

    #Login
    path('Registro/usuarios',RegistroLogin),
    path('Ingresar/usuarios',IngresarLogin),
    path('Cerrar/sesion',Logout),
    
    #Actualizar Perfil
    path('Actualizar/usuarios/<int:user_id>',ActualizarUsuario),
    path('Usuarios/eliminar/<int:user_id>',EliminarUsuario),

    #Principal
    path('Principal/inicio',Principal),
    path('Usuarios/contacto',Contacto, name='Contacto')
    

]
