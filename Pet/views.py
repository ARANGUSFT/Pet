from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


#region Elegir

#FUNCION PARA ENTRAR ELEGIR
def Elegir(request):    
    return render(request, 'Login/elegir.html')

#endregion


#region Principal

#FUNCION PARA ENTRAR A LA PAGINA PRINCIPAL
def Principal(request):    
    return render(request, 'Principal/inicio.html')

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
            return redirect(f"/Actualizar/usuarios/{user.id}")
        
        if User.objects.exclude(id=user_id).filter(email=email).exists():
            messages.error(request, 'El email ya fue registrado')
            return redirect(f"/Actualizar/usuarios/{user.id}")

        
        user = User.objects.get(id=user_id)
        user.username = username
        user.email = email
        user.password = password
        user.save()

        return redirect(f"/Actualizar/usuarios/{user.id}")

    # si el método de la petición es GET, mostrar el formulario de actualización de perfil
    else:
        if str(user.id) != str(user_id):
            return redirect('/Error/paginaerror')
        
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