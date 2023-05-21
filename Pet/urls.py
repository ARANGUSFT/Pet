
from django.contrib import admin
from django.urls import path
from Pet.views import Principal,Contacto,Contacto2
from Pet.views import Elegir,RegistroLogin,IngresarLogin,Logout,ActualizarUsuario,EliminarUsuario,ElegirBotones,InsertarMascota
from Pet.views import ListadoMascota,EliminarMascota,MostrarActualizarMascota,ActualizarMascota,InsertarDueño,InsertarEstiloPlaca,generar_pdf
from Pet.views import Envio,DatosCompra
from django.conf import settings
from django.conf.urls.static import static


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
    #Eliminar cuenta
    path('Usuarios/eliminar/<int:user_id>',EliminarUsuario),
    #Principal
    path('Principal/inicio',Principal),
    #Formularios Reporte
    path('Usuarios/contacto',Contacto, name='Contacto'),
    path('Usuarios/contacto2',Contacto2, name='Contacto2'),    


    #Elegir botones
    path('MisMascotas/Botones',ElegirBotones),
    #Insertar Mascota
    path('MisMascotas/Insertar',InsertarMascota),
    #Listado Mascota
    path('MisMascotas/Listado',ListadoMascota),
    #Borrar Mascota
    path('MisMascotas/Eliminar/<int:Id_Mascota>',EliminarMascota),  
    #Ver Actualizar Mascota
    path('MisMascotas/ActualizarForm/<int:Id_Mascota>',MostrarActualizarMascota),
    #Actualizar Mascota
    path('MisMascotas/Actualizar/<int:Id_Mascota>',ActualizarMascota),
    #Insertar Dueño
    path('MisMascotas/GenerarMiQR',InsertarDueño),
    #Insertar Estilo Placa
    path('MisMascotas/EstiloPlaca',InsertarEstiloPlaca),
    #Envio
    path('Envio/Datos',Envio),
    #Pasarela Pago
    path('Pago/Placa',DatosCompra),
    #Factura
    path('MisMascotas/Factura',generar_pdf)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
