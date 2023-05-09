//Obtenemos el elemento select y la imagen
const select = document.getElementById("Estilo_Color_C");
const imagen = document.getElementById("imagenes2");

//Escuchamos el evento cambio del select
select.addEventListener("change", function(){
  //Obtenemos el valor seleccionado y actualizamos la imagen
  const valor = select.value;
  imagen.src = valor;
  imagen.alt = select.options[select.selectedIndex].text;
});
