const imagen = document.getElementById('Estilo_Placa_C');
const imagenSeleccionada = document.getElementById('imagenes1');

imagen.addEventListener('change', function () {
    const valorSeleccionado = imagen.value;
    imagenSeleccionada.src = "{% static '" + valorSeleccionado + "' %}";
    imagenSeleccionada.alt = imagen.options[imagen.selectedIndex].text;
}); 