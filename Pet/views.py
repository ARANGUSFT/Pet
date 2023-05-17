from django.db import connection
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from Pet.models import Mascota,Dueno,Caracteristicas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.handlers.wsgi import WSGIRequest



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
        

def ListadoMascota(request):
    MascotasPorPaginar = 4
    MMascotas = Mascota.objects.filter(usuario=request.user) # solo las mascotas del usuario actual
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

#endregion


#region Placa
def InsertarEstiloPlaca(request):
   return render(request, 'MisMascotas/EstiloPlaca.html')
   """  if request.method == "POST":
   return render(request, 'MisMascotas/EstiloPlaca.html')
   """  if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.callproc('InsertarEstilos', [request.POST.get('Estilo_Placa_C'), request.POST.get('Color_Placa_C')])
        return redirect('/MisMascotas/Botones') """
    

#endregion

