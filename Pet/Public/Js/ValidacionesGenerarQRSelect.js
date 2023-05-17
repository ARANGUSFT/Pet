function validarSelect() {
    var selectValor = document.getElementById("MascotaDueño").value;
    var selectValor2 = document.getElementById("Municipio_D").value;

    if (selectValor === "") {
      document.querySelector('#Error1').style.display = 'block';
      document.getElementById('Error1').textContent = 'Debes elegir una de tus mascotas';
      return false;
    } else {
      document.querySelector('#Error1').style.display = 'none';
    }
    
    if (selectValor2 === "") {
      document.getElementById('Error6').textContent = 'Debes elegir un municipio';
      document.querySelector('#Error6').style.display = 'block';
      return false;
    } else {
      document.querySelector('#Error6').style.display = 'none';
    }

  }