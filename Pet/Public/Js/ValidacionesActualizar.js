const form = document.getElementById('formulario');

const expresiones = {
    expr1: /^[a-zA-Z]{1,50}$/,
    expr2: /^[A-Za-z][A-Za-z ]{0,48}[A-Za-z]$/,
    expr3: /^(?=.{1,50}$)([a-zA-Z]|[a-zA-Z][ ]{0,1}[a-zA-Z][ ]{0,1}[a-zA-Z]){1,50}$/,
}

function validateForm(event) {
    event.preventDefault();

    const NombreMascota = document.getElementById('NombreMascota');
    const RazaMascota = document.getElementById('RazaMascota');
    const ColorMascota = document.getElementById('ColorMascota');
    const FotoMacota = document.getElementById('FotoMacota');

    let validForm = true;
    //validacion del nombre nombre
    if (!expresiones.expr1.test(NombreMascota.value)) {
        document.getElementById('Error1').textContent = 'Debes ingresar un nombre valido , Verifique.';
        document.querySelector('#Error1').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error1').textContent = '';
        document.querySelector('#Error1').style.display = 'none';
    }
    //validacion de la raza
    if (!expresiones.expr2.test(RazaMascota.value)) {
        document.getElementById('Error2').textContent = 'Debes ingresar una raza valida, Verifique.';
        document.querySelector('#Error2').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error2').textContent = '';
        document.querySelector('#Error2').style.display = 'none';
    }
    //validacion de el color
    if (!expresiones.expr3.test(ColorMascota.value)) {
        document.getElementById('Error3').textContent = 'Debes ingresar color valido, Verifique.';
        document.querySelector('#Error3').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error3').textContent = '';
        document.querySelector('#Error3').style.display = 'none';
    }
    //Validacion de la foto mascota

    if (validForm) {
        swal({
            title: "¿Estas seguro de los cambios que hiciste?",
            text: "Verifica antes de enviarlos",
            icon: "warning",
            buttons: ["Cancelar", "Enviar"],
            dangerMode: true,
        })
            .then((willSubmit) => {
                if (willSubmit) {
                    form.submit();
                } else {
                    // No hacer nada
                }
            });
    }
}


form.addEventListener('submit', validateForm);