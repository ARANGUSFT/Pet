from django.db import connection
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from Pet.models import Mascota,Dueno,Caracteristicas,Envio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import qrcode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.shortcuts import render, get_object_or_404
from io import BytesIO



#region Elegir

#FUNCION PARA ENTRAR ELEGIR
def Elegir(request):    
    return render(request, 'Login/elegir.html')

#endregion


#region Principal

#FUNCION PARA ENTRAR A LA PAGINA PRINCIPAL
def Principal(request):    
    return render(request, 'Principal/inicio.html')



#FUNCION PARA MANDAR EL CORREO
def Contacto(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('Principal/email.html',{
            'name': name,
            'email': email,
            'message': message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['littlepetworld2023@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Correo enviado')
        return redirect('/Usuarios/contacto')
    else:
        return render(request, 'Principal/contacto.html')
    
    
def Contacto2(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('Principal/email.html',{
            'name': name,
            'email': email,
            'message': message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['littlepetworld2023@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Correo enviado')
        return redirect('/Usuarios/contacto2')
    else:
        return render(request, 'Principal/contacto2.html')


#endregion


#region Login


#FUNCION PARA REGISTRO
def RegistroLogin(request):
    if request.method == "POST":
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Verifica si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request,'El apodo ya esta en uso')
            return redirect('/Registro/usuarios')
        
        if User.objects.filter(email=email).exists():
            messages.success(request,'El email ya fue registrado')
            return redirect('/Registro/usuarios')

        usuario = User.objects.create_user(username=username, email=email, password=password)
        usuario.save()

        return redirect('/Ingresar/usuarios')
    else:
        return render(request,'Login/registro.html')
    


#FUNCION PARA VALIDACION LOGIN
def IngresarLogin(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/Principal/inicio')
        else:
            mensaje = "Revisa bien el apodo y la contraseña"
            return render(request,'Login/ingresar.html',{'mensaje':mensaje})
    
     else:
        return render(request,'Login/ingresar.html')
     


#FUNCION PARA CERRAR SESION
def Logout(request):
    logout(request)
    return redirect('/Elegir/entrar')

#endregion


#region Actualizar Perfil

def ActualizarUsuario(request, user_id):
    # obtener el usuario actual
    user = request.user
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        #Validacion
        user = authenticate(request, username=username, password=password)

        if User.objects.exclude(id=user_id).filter(username=username).exists():
            messages.error(request, 'El apodo ya esta en uso')
            return redirect(f"/Actualizar/usuarios/{user_id}")
        
        if User.objects.exclude(id=user_id).filter(email=email).exists():
            messages.error(request, 'El email ya fue registrado')
            return redirect(f"/Actualizar/usuarios/{user_id}")

        user = User.objects.get(id=user_id)
        user.username = username
        user.email = email
        user.set_password(password)  # Utilizamos el método set_password() para establecer la nueva contraseña
        user.save()

        # Autenticar al usuario con su nueva contraseña
        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            # Iniciar sesión con la nueva información de autenticación
            login(request, auth_user)
            # Actualizar la sesión del usuario con la nueva información de autenticación
            update_session_auth_hash(request, auth_user)

        return redirect(f"/Actualizar/usuarios/{user.id}")
    else:
        if str(user.id) != str(user_id):
            return redirect(f"/Actualizar/usuarios/{user.id}")

        else:
          user = User.objects.get(id=user_id)
          return render(request, 'Login/actualizar.html', {'user': user})

        

#endregion


#region EliminarCuenta

def EliminarUsuario(request,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/Elegir/entrar')

#endregion


#region MisMascotas
def ElegirBotones(request):    
    return render(request, 'MisMascotas/Botones.html')


def InsertarMascota(request):
    if request.method == "POST":
        # ...
        mascota = Mascota()
        mascota.Nombre_M = request.POST.get('Nombre_M')
        mascota.Raza_M = request.POST.get('Raza_M')
        mascota.Color_M = request.POST.get('Color_M')
        mascota.Foto_M = request.FILES['Foto_M']
        mascota.usuario = request.user  # asociar la mascota con el usuario actual
        mascota.save()

        # Generar el código QR con el enlace a la vista de detalles
        mascota_id = mascota.pk  # Asegúrate de que la variable 'mascota' esté definida aquí
        qr_code_data = f"http://127.0.0.1:8000/MisMascotas/Listado/{mascota_id}"
        qr_code_file = f"mascota_{mascota_id}.png"

        qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr_code.add_data(qr_code_data)
        qr_code.make(fit=True)
        qr_image = qr_code.make_image(fill_color="black", back_color="white")
        qr_image.save(f"Pet/Public/QrCode/{qr_code_file}")

        return redirect('/MisMascotas/Listado')
    else:
        return render(request, 'MisMascotas/Insertar.html')
        

def ListadoMascota(request):
    MascotasPorPaginar = 4
    MMascotas = Mascota.objects.filter(usuario=request.user)  # solo las mascotas del usuario actual
    paginador = Paginator(MMascotas, MascotasPorPaginar)

    pagina = request.GET.get('pagina')

    try:
        mascotas = paginador.page(pagina)
    except PageNotAnInteger:
        mascotas = paginador.page(1)
    except EmptyPage:
        mascotas = paginador.page(paginador.num_pages)

    context = {
        'mascotas': mascotas
    }

    return render(request, 'MisMascotas/Listado.html', context)


#Vista del QR
def DetalleMascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, Id_Mascota=mascota_id)

    context = {
        'mascota': mascota
    }

    return render(request, 'MisMascotas/Detalle.html', context)



def EliminarMascota(request,Id_Mascota):
    
        mascota = Mascota.objects.get(Id_Mascota = Id_Mascota)
        Nombre_M = mascota.Nombre_M
        Raza_M = mascota.Raza_M
        Color_M = mascota.Color_M
        ruta_foto = "Media/"+str(mascota.Foto_M)
        mascota.delete()
        
        import os
        if ruta_foto != "Media/ImagenesBD/noimagen.jpg":
            os.remove(ruta_foto)
            
        mascota = Mascota.objects.all().values()
        context = {
        'mascotas': mascota
        }
        
        return render(request, 'MisMascotas/Listado.html', context)


    
def MostrarActualizarMascota(request,Id_Mascota):
    mascota = Mascota.objects.get(Id_Mascota = Id_Mascota)
    context = {
        'mascota': mascota
    }
    return render(request, 'MisMascotas/Actualizar.html', context)



def ActualizarMascota(request, Id_Mascota):
    try:
        Nombre_M = request.POST['Nombre_M']
        Raza_M = request.POST['Raza_M']
        Color_M = request.POST['Color_M']
        mascota = Mascota.objects.get(Id_Mascota=Id_Mascota)

        try:
            Foto_M = request.FILES['Foto_M']
            ruta_foto = "Media/" + str(mascota.Foto_M)
            import os
            if ruta_foto != "Media/ImagenesBD/noimagen.jpg":
                os.remove(ruta_foto)
        except:
            Foto_M = mascota.Foto_M

        mascota.Nombre_M = Nombre_M
        mascota.Raza_M = Raza_M
        mascota.Color_M = Color_M
        mascota.Foto_M = Foto_M
        mascota.usuario = request.user  # Asigna el usuario actual a la mascota actualizada
        mascota.save()

        mascotas = Mascota.objects.filter(usuario=request.user).values()

        context = {
            'mascotas': mascotas
        }
        return render(request, 'MisMascotas/Listado.html', context)
    except:
        pass

#endregion


# //UNIR LA MASCOTA SELECCIONADA Y QUE APAREZCA SU QR EN LA FACTURA#
#region Dueño
def InsertarDueño(request):
    
    if request.method == "POST":
         #prepar
     
        insertar = connection.cursor()
        insertar.execute("call insertarDueno('"+request.POST.get ('Nombre_Completo_D')+"','"+request.POST.get ('Celular_D')+"','"+request.POST.get ('Celular_Secundario_D')+"','"+request.POST.get ('Correo_D')+"','"+request.POST.get ('Municipio_D')+"','"+request.POST.get ('Mascota_Id')+"')")
        return redirect('/MisMascotas/EstiloPlaca')
    else:
        mascota = Mascota.objects.filter(usuario=request.user)
        return render(request,'MisMascotas/GenerarMiQR.html',{'mascota':mascota})
    
def vista_anterior(request):
    if request.method == 'GET':
        # Elimina el registro de la base de datos
        Dueno.objects.last().delete()
        
    return redirect('/MisMascotas/GenerarMiQR')
#endregion


#region Placa

def InsertarEstiloPlaca(request):
    if request.method == "POST":
        caracteristica = Caracteristicas()
        caracteristica.Estilo_Placa_C = request.POST.get('Estilo_Placa_C')
        caracteristica.Estilo_Color_C = request.POST.get('Color_Placa_C')
        caracteristica.Dueno_Id = Dueno.objects.get(Id_Dueno=request.POST.get('Dueno_Id'))

        caracteristica.save()
        return redirect('Envio/Datos')
    else:
            return render(request, 'MisMascotas/EstiloPlaca.html')

#endregion  


#region Envio

def DatosEnvio(request):
        if request.method == "POST":
            Datos = Envio()
            Datos.Direccion = request.POST.get('dire')
            Datos.Barrio = request.POST.get('barri')
            Datos.Detalles = request.POST.get('detalle')
            Datos.save()
            return redirect('/Pago/Placa')
        else:
            return render (request, 'Envio/DatosEnvio.html')
        

#endregion


#AQUI DEBE APARECER EL QR Y LOS DATOS DEL USUARIO
#region Pdf

def generar_factura(request):

    datos_factura = {
    'numero_factura': 'F2023001',
    'fecha_emision': '22 de mayo de 2023',
    'cliente': {
        'nombre': 'Juan Pérez',
        'direccion': 'Calle Principal, 123',
        'ciudad': 'Ciudad XYZ',
        'telefono': '1234567890'
    },
    'items': [
        {
            'descripcion': 'Producto A',
            'cantidad': 2,
            'precio_unitario': 10.00,
            'subtotal': 20.00
        },
        {
            'descripcion': 'Producto B',
            'cantidad': 3,
            'precio_unitario': 15.00,
            'subtotal': 45.00
        },
        # Agrega más elementos de línea de factura según sea necesario
    ],
    'total': 65.00  # Total de la factura
  }
    
    mascota = Mascota.objects.filter(usuario=request.user).first()

    # Verifica si se encontró una mascota para el usuario actual
    if mascota:
        # Generar el código QR con el enlace a la vista de detalles de la mascota
        mascota_id = mascota.pk
        qr_code_data = f"http://127.0.0.1:8000/MisMascotas/Listado/{mascota_id}"
        qr_code_file = f"mascota_{mascota_id}.png"

        qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr_code.add_data(qr_code_data)
        qr_code.make(fit=True)
        qr_image = qr_code.make_image(fill_color="black", back_color="white")
        qr_image.save(f"Pet/Public/QrCode/{qr_code_file}")

        # Carga la plantilla HTML de la factura
        template = get_template('Factura/archivo.html')
        context = {
            'datos_factura': datos_factura,  # Reemplaza con los datos relevantes de la factura
            'qr_code_url': f"/Pet/Public/QrCode/{qr_code_file}",  # Actualiza la URL del código QR
        }
        html = template.render(context)

        # Crea un objeto BytesIO para almacenar el PDF generado
        pdf_file = BytesIO()

        # Genera el PDF a partir del HTML de la factura y el código QR
        pisa.CreatePDF(html, dest=pdf_file)

        # Vuelve al inicio del archivo PDF generado
        pdf_file.seek(0)

        # Crea un objeto HttpResponse con el encabezado adecuado para PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="factura.pdf"'

        # Copia el contenido del archivo PDF generado al objeto de respuesta
        response.write(pdf_file.read())

        return response
        # else:
        #     # No se encontró una mascota asociada al usuario actual
        #     # Maneja este caso según tus necesidades (por ejemplo, muestra un mensaje de error)

#endregion





