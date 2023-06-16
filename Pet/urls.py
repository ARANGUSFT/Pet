
from django.contrib import admin
from django.urls import path
from Pet.views import Principal,Contacto,Contacto2
from Pet.views import Elegir,RegistroLogin,IngresarLogin,Logout,ActualizarUsuario,EliminarUsuario,ElegirBotones,InsertarMascota
from Pet.views import ListadoMascota,EliminarMascota,MostrarActualizarMascota,ActualizarMascota,InsertarDueño,InsertarEstiloPlaca,generar_factura,vista_anterior
from Pet.views import DatosEnvio,CompraRealizada
from . import views
from Pet.views import vista_anterior2,vista_anterior3
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


    #Vista del QR, individual por mascota
    path('MisMascotas/Listado/<int:mascota_id>/<int:dueno_id>/', views.DetalleMascota, name='detalle_mascota'),


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
    path('Envio/Datos',DatosEnvio),


    
    #Factura
    path('Compra/realizada',CompraRealizada),
    path('generar/factura', generar_factura, name='generar_factura'),
    

    #Vista anterior
    path('MisMascotas/vista_anterior',vista_anterior),
    #Vista anterior2
    path('MisMascotas/vista_anterior2',vista_anterior2),
    #Vista anterior3
    path('MisMascotas/vista_anterior3',vista_anterior3)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
