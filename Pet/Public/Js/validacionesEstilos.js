const form = document.getElementById('formulario');

function validateForm(event) {
    event.preventDefault();


    var selectValor = document.getElementById("select-imagen").value;
    var selectValor2 = document.getElementById("select-Color").value;
    

    let validForm = true;

    //validacion de la mascota
    if (selectValor === "") {
        document.querySelector('#Error1').style.display = 'block';
        document.getElementById('Error1').textContent = 'Debes elegir un estilo para tu placa, Verifica.';
        validForm = false;
    } else {
        document.querySelector('#Error1').style.display = 'none';
    }

     //validacion del municipio 
     if (selectValor2 === "") {
        document.querySelector('#Error2').style.display = 'block';
        document.getElementById('Error2').textContent = 'Debes elegir un color para tu placa, Verifica.';
        validForm = false;
    } else {
        document.querySelector('#Error2').style.display = 'none';
    }

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



form.addEventListener('submit', validateForm);