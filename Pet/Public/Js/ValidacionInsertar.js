const form = document.getElementById('formulario');

const expresiones = {
    expr1: /^[a-zA-Z]{1,50}$/,
    expr2: /^[a-zA-Z]{1,50}$/,
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
        document.getElementById('Error1').textContent = 'El Nombre no puede llevar numeros, carecteres especiales, espacios en blanco ni ir vacio, Verifique.';
        document.querySelector('#Error1').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error1').textContent = '';
        document.querySelector('#Error1').style.display = 'none';
    }
    //validacion de la raza
    if (!expresiones.expr2.test(RazaMascota.value)) {
        document.getElementById('Error2').textContent = 'La raza no puede llevar numeros, carecteres especiales, espacios en blanco ni ir vacio, Verifique.';
        document.querySelector('#Error2').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error2').textContent = '';
        document.querySelector('#Error2').style.display = 'none';
    }
    //validacion de el color
    if (!expresiones.expr3.test(ColorMascota.value)) {
        document.getElementById('Error3').textContent = 'El color no puede llevar numeros, carecteres especiales, espacios en blanco ni ir vacio, Verifique.';
        document.querySelector('#Error3').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error3').textContent = '';
        document.querySelector('#Error3').style.display = 'none';
    }
    //Validacion de la foto mascota
    const file = FotoMacota.files[0];
    const imageTypes = ['image/jpeg', 'image/png', 'image/jpg'];
    if (!file || !imageTypes.includes(file.type)) {
        document.getElementById('Error4').textContent = 'La foto de la mascota debe ser (Jpeg, png, jpg) ni ir vacio, Verifique.';
        document.querySelector('#Error4').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error4').textContent = '';
        document.querySelector('#Error4').style.display = 'none';
    }

    if (validForm) {
        swal({
            title: "¿Estas seguro de registrar a tu mascota?",
            text: "Verifica los datos de mascota antes de enviarlos",
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