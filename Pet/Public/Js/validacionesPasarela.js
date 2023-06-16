const form = document.getElementById('formulario');

const expresiones = {
    expr1: /^([A-Za-z]+ [A-Za-z]+ [A-Za-z]+ [A-Za-z]+)|([A-Za-z]+ [A-Za-z]+ [A-Za-z]+)|([A-Za-z]+ de [A-Za-z]+ [A-Za-z]+ [A-Za-z]+)$/,
    expr2: /^(\d{4}-){3}\d{4}$/,
    expr3: /^\d{2}$/,
    expr4: /^\d{3}$/
}

function validateForm(event) {
    event.preventDefault();

    const Nombre = document.getElementById('Nombre');
    const NumeroTarjeta = document.getElementById('NumeroTarjeta');
    const Fecha = document.getElementById('Fecha');
    const Codigo = document.getElementById('Codigo');

    let validForm = true;
    //validacion del nombre
    if (!expresiones.expr1.test(Nombre.value)) {
        document.getElementById('Error1').textContent = 'Debes ingresa un nombre valido, Verifique.';
        document.querySelector('#Error1').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error1').textContent = '';
        document.querySelector('#Error1').style.display = 'none';
    }
    //validacion de la raza
    if (!expresiones.expr2.test(NumeroTarjeta.value)) {
        document.getElementById('Error2').textContent = 'Debes ingresa un numero de tarejta valido, Verifique.';
        document.querySelector('#Error2').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error2').textContent = '';
        document.querySelector('#Error2').style.display = 'none';
    }
    //validacion de el color
    if (!expresiones.expr3.test(Fecha.value)) {
        document.getElementById('Error3').textContent = 'Debes ingresar una fecha valida, Verifique.';
        document.querySelector('#Error3').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error3').textContent = '';
        document.querySelector('#Error3').style.display = 'none';
    }
    //Validacion de la foto mascota
    if (!expresiones.expr4.test(Codigo.value)) {
        document.getElementById('Error4').textContent = 'Debes ingresar un codigo de seguridad valido, Verifique.';
        document.querySelector('#Error4').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error4').textContent = '';
        document.querySelector('#Error4').style.display = 'none';
    }

    if (validForm) {
        swal({
            title: "¿Estás seguro de realizar la compra?",
            text: "Después de realizar la compra no se puede cancelar y se generará tu factura",
            icon: "warning",
            buttons: ["Cancelar", "Finalizar"],
            dangerMode: true,
        })
        .then((willSubmit) => {
            if (willSubmit) {
                // Realizar la redirección
                window.location.href = "/Compra/realizada";
            } else {
                // No hacer nada
            }
        });
    }
    
    
}


form.addEventListener('submit', validateForm);