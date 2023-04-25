const form = document.getElementById('form');

const expresiones = {
    expr1 : /^[\w\d\s!"#$%&'()*+,\-.\/:;<=>?@\[\]^_`{|}~]{1,20}$/i,
	expr2 : /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	expr3 : /^[\w\d\s!"#$%&'()*+,\-.\/:;<=>?@\[\]^_`{|}~]{8,16}$/i
}

function validateForm(event)  {
    event.preventDefault();

    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');

    let validForm = true;
    //validacion del nombre dueño
    if (!expresiones.expr1.test(username.value)) {
        document.getElementById('Error1').textContent = 'El Apodo no puede ir vacio';
        document.querySelector('#Error1').style.display = 'block';
        validForm = false;
      } else {
        document.getElementById('Error1').textContent = '';
        document.querySelector('#Error1').style.display = 'none';
      }
    //validacion del correo dueño
      if (!expresiones.expr2.test(email.value)) {
        document.getElementById('Error2').textContent = 'El Correo no puede ir vacio tiene que llevar la estructura basica del gmail';
        document.querySelector('#Error2').style.display = 'block';
        validForm = false;
      } else {
        document.getElementById('Error2').textContent = '';
        document.querySelector('#Error2').style.display = 'none';
      }
    //validacion del celular dueño
      if (!expresiones.expr3.test(password.value)) {
        document.getElementById('Error3').textContent = 'La contraseña no puede ir vacia y tiene un minimo de 8 carateres y un maximo de 16 caracteres';
        document.querySelector('#Error3').style.display = 'block';
        validForm = false;
      } else {
        document.getElementById('Error3').textContent = '';
        document.querySelector('#Error3').style.display = 'none';
      }

      
      if (validForm) {
        // Si el formulario es válido, se puede enviar
        form.submit();
      }
}

form.addEventListener('submit', validateForm);


