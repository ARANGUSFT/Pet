const select = document.getElementById("seleccion");
const imagen = document.getElementById("imagen");

select.addEventListener("change", function(){
    const valor = select.value;
    imagen.src = "{% static '" + valor + "'%}";
    imagen.alt = select.options[select.selectedIndex].text;
}); 