const select = document.getElementById("select-imagen");
const imagen = document.getElementById("imagen-seleccionada");

select.addEventListener("change", function () {
    const valor = select.value;
    imagen.src = "{% static '" + valor + "'%}";
    imagen.alt = select.options[select.selectedIndex].text;
}); 
