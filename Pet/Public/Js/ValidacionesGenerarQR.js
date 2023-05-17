const form = document.getElementById('formulario');

const expresiones = {
    expr1: /^([A-Za-z]+ [A-Za-z]+ [A-Za-z]+ [A-Za-z]+)|([A-Za-z]+ [A-Za-z]+ [A-Za-z]+)|([A-Za-z]+ de [A-Za-z]+ [A-Za-z]+ [A-Za-z]+)$/,
    expr2: /^3\d{9}$/,
    expr3: /^3\d{9}$/,
    expr4: /^[^\s@]+@[^\s@]+\.[^\s@]+$/
}

function validateForm(event) {
    event.preventDefault();

    
    const NombreDueño = document.getElementById('NombreDueño');
    const CelularDueño = document.getElementById('CelularDueño');
    const CelularSecundiario = document.getElementById('CelularSecundiario');
    const CorreoDueño = document.getElementById('CorreoDueño');
    
    let validForm = true;

    //validacion del nombre del dueño
    if (!expresiones.expr1.test(NombreDueño.value)) {
        document.getElementById('Error2').textContent = 'debe ser tu nombre completo, no puede llevar numeros, carecteres especiales, espacios en blanco al principio o final ni ir vacio, Verifique.';
        document.querySelector('#Error2').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error2').textContent = '';
        document.querySelector('#Error2').style.display = 'none';
    }

    //validacion del celular
    if (!expresiones.expr2.test(CelularDueño.value)) {
        document.getElementById('Error3').textContent = 'no puede llevar letras, carecteres especiales, espacios en blanco ni ir vacio debe empezar por 3 y un total de 10 digitos, Verifique.';
        document.querySelector('#Error3').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error3').textContent = '';
        document.querySelector('#Error3').style.display = 'none';
    }

    //validacion del celular secundario
    if (!expresiones.expr3.test(CelularSecundiario.value)) {
        document.getElementById('Error4').textContent = 'no puede llevar letras, carecteres especiales, espacios en blanco ni ir vacio debe empezar por 3 y un total de 10 digitos, Verifique.';
        document.querySelector('#Error4').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error4').textContent = '';
        document.querySelector('#Error4').style.display = 'none';
    }

    //Validacion del correo
    if (!expresiones.expr4.test(CorreoDueño.value)) {
        document.getElementById('Error5').textContent = 'debe cumplir con la estructura de un correo electronico, espacios en blanco  ni ir vacio, Verifique.';
        document.querySelector('#Error5').style.display = 'block';
        validForm = false;
    } else {
        document.getElementById('Error5').textContent = '';
        document.querySelector('#Error5').style.display = 'none';

 

    if (validForm) {
        swal({
            title: "Verifica los datos diligenciados",
            text: "!Despues de enviados no puedes cambiar la informacion grabada en el QR¡",
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
}

form.addEventListener('submit', validateForm);


/*   //validacion del nombre mascota
    if (selectedValue === '') {
        event.preventDefault(); // previene el envío del formulario
        document.querySelector('#Error1').style.display = 'block';
        document.getElementById('Error1').textContent = 'Tienes que elegir una de tus mascotas';
      }else{
        document.querySelector('#Error1').style.display = 'none';
      } */

/* //validacion del municipio
    if (selectedValue2 === '') {
        event.preventDefault(); // previene el envío del formulario
        document.getElementById('Error6').textContent = 'El color no lo puedes enviar vacio';
        document.querySelector('#Error6').style.display = 'block';
      }else{
        document.querySelector('#Error6').style.display = 'none';
      } */

/* 
    const MunicipioDueño = document.getElementById('MunicipioDueño');
    const MascotaDueño = document.getElementById('MascotaDueño');
    const selectedValue = MascotaDueño.value;
    const selectedValue2 = MunicipioDueño.value; */