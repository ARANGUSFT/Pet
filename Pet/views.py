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
from django.contrib.auth.decorators import login_required
from urllib.parse import urljoin





#region Elegir

#FUNCION PARA ENTRAR ELEGIR
def Elegir(request):    
    return render(request, 'Login/elegir.html')

#endregion


#region Principal

#FUNCION PARA ENTRAR A LA PAGINA PRINCIPAL
@login_required(login_url='/Elegir/entrar')
def Principal(request):    
    return render(request, 'Principal/inicio.html')



#FUNCION PARA MANDAR EL CORREO
@login_required(login_url='/Elegir/entrar')
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
    if request.user.is_authenticated:
        logout(request)
    return redirect('/Elegir/entrar')

#endregion


#region Actualizar Perfil
@login_required(login_url='/Elegir/entrar')
def ActualizarUsuario(request, user_id):
    # Obtener el usuario actual
    user = request.user

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Validación
        if User.objects.exclude(id=user_id).filter(username=username).exists():
            messages.error(request, 'El apodo ya está en uso')
            return redirect(f"/Actualizar/usuarios/{user_id}")

        if User.objects.exclude(id=user_id).filter(email=email).exists():
            messages.error(request, 'El email ya fue registrado')
            return redirect(f"/Actualizar/usuarios/{user_id}")

        user = User.objects.get(id=user_id)
        user.username = username
        user.email = email

        if password:
            user.set_password(password)  # Utilizamos el método set_password() para establecer la nueva contraseña

        user.save()

        # Autenticar al usuario con su nueva información
        if password:
            # Solo si se proporcionó una nueva contraseña
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
@login_required(login_url='/Elegir/entrar')
def EliminarUsuario(request,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/Elegir/entrar')

#endregion


#region MisMascotas
@login_required(login_url='/Elegir/entrar')
def ElegirBotones(request):    
    return render(request, 'MisMascotas/Botones.html')

@login_required(login_url='/Elegir/entrar')
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
        return redirect('/MisMascotas/Listado')
    else:
        return render(request, 'MisMascotas/Insertar.html')


@login_required(login_url='/Elegir/entrar')
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



@login_required(login_url='/Elegir/entrar')
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


@login_required(login_url='/Elegir/entrar')   
def MostrarActualizarMascota(request,Id_Mascota):
    mascota = Mascota.objects.get(Id_Mascota = Id_Mascota)
    context = {
        'mascota': mascota
    }
    return render(request, 'MisMascotas/Actualizar.html', context)


@login_required(login_url='/Elegir/entrar')
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


#region Dueño
@login_required(login_url='/Elegir/entrar')
def InsertarDueño(request):
    if request.method == "POST":
        nombre_completo = request.POST.get('Nombre_Completo_D')
        celular_d = request.POST.get('Celular_D')
        celular_secundario_d = request.POST.get('Celular_Secundario_D')
        correo_d = request.POST.get('Correo_D')
        municipio_d = request.POST.get('Municipio_D')
        mascota_id = request.POST.get('Mascota_Id')
       
        mascota = Mascota.objects.get(Id_Mascota=mascota_id)  

        dueno = Dueno.objects.create(
            Nombre_Completo_D=nombre_completo,
            Celular_D=celular_d,
            Celular_Secundario_D=celular_secundario_d,
            Correo_D=correo_d,
            Municipio_D=municipio_d,
            Mascota_Id=mascota
        )

        # Obtener el ID del dueño recién creado
        dueno_id = dueno.pk

        # Generar el código QR con el enlace a la vista de detalles
        qr_code_data = f"http://127.0.0.1:8000/MisMascotas/Listado/{mascota_id}/{dueno_id}"
        qr_code_file = f"mascota_{mascota_id}.png"

        qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr_code.add_data(qr_code_data)
        qr_code.make(fit=True)
        qr_image = qr_code.make_image(fill_color="black", back_color="white")


        # Guardar el código QR en la carpeta de medios
        qr_code_path = os.path.join(settings.MEDIA_ROOT, qr_code_file)
        qr_image.save(qr_code_path)

        # Asociar la información del código QR al modelo Dueno
        dueno.codigo_qr_url = urljoin(settings.MEDIA_URL, qr_code_data)
        dueno.codigo_qr_nombre_archivo = qr_code_file
        dueno.save()



        return redirect('/MisMascotas/EstiloPlaca')
    else:
        mascota = Mascota.objects.filter(usuario=request.user)
        return render(request, 'MisMascotas/GenerarMiQR.html', {'mascota': mascota})

    


@login_required(login_url='/Elegir/entrar')
def vista_anterior(request):
    if request.method == 'GET':
        # Elimina el registro de la base de datos
        Dueno.objects.last().delete()
        
    return redirect('/MisMascotas/GenerarMiQR')
#endregion


#region QR Vista
def DetalleMascota(request, mascota_id, dueno_id):
    mascota = get_object_or_404(Mascota, Id_Mascota=mascota_id)
    dueno = get_object_or_404(Dueno, Id_Dueno=dueno_id)

    context = {
        'mascota': mascota,
        'dueno': dueno
    }

    return render(request, 'MisMascotas/Detalle.html', context)

#endregion


#region Placa


@login_required(login_url='/Elegir/entrar')
def InsertarEstiloPlaca(request):
    if request.method == "POST":
        caracteristica = Caracteristicas()
        caracteristica.Estilo_Placa_C = request.POST.get('Estilo_Placa_C')
        caracteristica.Estilo_Color_C = request.POST.get('Color_Placa_C')

        dueno = Dueno.objects.filter(Mascota_Id__usuario=request.user).last()  # Obtener el último dueño en lugar del primero
        caracteristica.Dueno_Id = dueno

        caracteristica.save()
        return redirect('/Envio/Datos')
    else:
        dueno = Dueno.objects.filter(Mascota_Id__usuario=request.user).last()  # Obtener el último dueño en lugar del primero
        return render(request, 'MisMascotas/EstiloPlaca.html', {'dueno': dueno})





    
    
@login_required(login_url='/Elegir/entrar')
def vista_anterior2(request):
    if request.method == 'GET':
        # Elimina el registro de la base de datos
        Caracteristicas.objects.last().delete()
        
    return redirect('/MisMascotas/EstiloPlaca')

#endregion  


#region Envio
@login_required(login_url='/Elegir/entrar')
def DatosEnvio(request):
        if request.method == "POST":
            Datos = Envio()
            Datos.Direccion = request.POST.get('dire')
            Datos.Barrio = request.POST.get('barri')
            Datos.Detalles = request.POST.get('detalle')
            # Datos.Caracteristicas_Id = Caracteristicas.objects.get(Id_Caracteristicas=request.POST.get('Caracteristicas_Id'))
            
            dueno = Dueno.objects.filter(Mascota_Id__usuario=request.user).first()
            Datos.Dueno_Id = dueno
             
            Datos.save()
            return redirect('/MisMascotas/Pasarela')
        else:
            dueno = Dueno.objects.filter(Mascota_Id__usuario=request.user).first()
            return render(request, 'Envio/DatosEnvio.html', {'dueno': dueno})
    
@login_required(login_url='/Elegir/entrar')
def vista_anterior3(request):
    if request.method == 'GET':
        # Elimina el registro de la base de datos
        Envio.objects.last().delete()
        
    return redirect('/Envio/Datos')        
#endregion


#region Pasarela
@login_required(login_url='/Elegir/entrar')
def payment_view(request):
    return render(request, 'MisMascotas/Pasarela.html')

#endregion


#region Pdf

def generar_factura(request):
    usuario = request.user

    # Obtener el último Dueño relacionado con el usuario en sesión
    dueno = Dueno.objects.filter(Mascota_Id__usuario=usuario).last()

    # Verificar si existe un Dueño para generar la factura
    if dueno is None:
        return HttpResponse("No se encontraron datos de compra.")

    mascota = dueno.Mascota_Id
    caracteristica = Caracteristicas.objects.filter(Dueno_Id=dueno).first()
    

    context = {
        'dueno': dueno,
        'mascota': mascota,
        'caracteristica': caracteristica
    }

    # Renderizar la plantilla HTML con los datos de la factura
    template_path = 'Factura/archivo.html'  # Ruta de la plantilla HTML
    html = render(request, template_path, context).content

    # Crear un archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="factura.pdf"'

    # Convertir el HTML a PDF usando xhtml2pdf
    pisa.CreatePDF(html, dest=response)

    return response



    
   

#endregion


#region CompraRealizada
@login_required(login_url='/Elegir/entrar')
def CompraRealizada(request):    
    return render(request, 'MisMascotas/CompraRealizada.html')

#endregion
