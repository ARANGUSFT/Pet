const form = document.getElementById('formulario');

function validateForm(event) {
    event.preventDefault();

    
    const MunicipioDueño = document.getElementById('MunicipioDueño');
    const MascotaDueño = document.getElementById('MascotaDueño');
    const selectedValue = MascotaDueño.value;
    const selectedValue2 = MunicipioDueño.value;

    let validForm = true;

    //validacion del nombre mascota
    if (selectedValue === '') {
        event.preventDefault(); // previene el envío del formulario
        document.querySelector('#Error1').style.display = 'block';
        document.getElementById('Error1').textContent = 'Debes elegir una de tus mascotas';
    } else {
        document.querySelector('#Error1').style.display = 'none';
    }

    //validacion del municipio
    if (selectedValue2 === '') {
        event.preventDefault(); // previene el envío del formulario
        document.getElementById('Error6').textContent = 'Debes elegir un municipio';
        document.querySelector('#Error6').style.display = 'block';
        validForm = false;
    } else {
        document.querySelector('#Error6').style.display = 'none';
    }
}

form.addEventListener('submit', validateForm);
