function validateForm(){
    document.getElementById("NombreMascotaError").textContent = "";
    document.getElementById("RazaMascotaError").textContent = "";
    document.getElementById("ColorMascotaError").textContent = "";
    document.getElementById("FotoMascotaError").textContent = "";
    document.getElementById("Error").textContent = "";

    var NombreMascota = document.forms["registrationForm"]["NombreMascota"].value;
    var RazaMascota = document.forms["registrationForm"]["RazaMascota"].value;
    var ColorMascota = document.forms["registrationForm"]["ColorMascota"].value;

    if (NombreMascota === "") {
        document.getElementById("NombreMascotaError").textContent = "Ingresa el nombre de la mascota";
        return false;
    } 
    
}

const Formulario = document.getElementById("form");

Formulario.addEventListener("submit", function (event) {
    event.preventDefault(); 


    
    Formulario.submit(); 
});











/*const Formulario = document.getElementById("form");

Formulario.addEventListener("submit", function (event) {
    event.preventDefault(); // Evita que el formulario se envíe de forma automática


    // Si todo está correcto, se envía el formulario
    Formulario.submit(); // Envía el formulario de forma programática
});


 
    var NombreMascota = document.getElementById("NombreMascota");
    var RazaMascota = document.getElementById("RazaMascota");
    var ColorMascota = document.getElementById("ColorMascota");
    const FotoMascota = document.getElementById('FotoMascota');


    const file = this.files[0];
    const fileType = file.type;
    const validTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'];

    if (!file) {
        document.getElementById("error-FotoMascota").innerHTML = "Por favor, seleccione un archivo.";
        FotoMascota.classList.add("error");
        return false; // Evita que el formulario se envíe

    } else {
        document.getElementById("error-FotoMascota").innerHTML = "";
        FotoMascota.classList.remove("error");
        FotoMascota.classList.add("valid");
    }

    if (!validTypes.includes(fileType)) {
        alert('Solo se permiten archivos de imagen (JPEG, PNG, GIF) y archivos PDF.');
        this.value = '';
    } */
