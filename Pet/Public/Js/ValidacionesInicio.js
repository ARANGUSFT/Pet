function validateForm() {
    // Reset error messages
    document.getElementById("usernameError").textContent = "";
    document.getElementById("passwordError").textContent = "";

    // Get form values
    var username = document.forms["registrationForm"]["username"].value;
    var password = document.forms["registrationForm"]["password"].value;

    // Validate username
    if (username === "") {
      document.getElementById("usernameError").textContent = "Por favor, ingresa su nombre de usuario.";
      return false;
    } else if (username.length < 4) {
      document.getElementById("usernameError").textContent = "Recuerda que el nombre es de 4 o mas caracteres";
      return false;
    }

 
    // Validate password
    if (password === "") {
      document.getElementById("passwordError").textContent = "Por favor, ingresa una contraseña.";
      return false;
    } else if (password.length < 8) {
      document.getElementById("passwordError").textContent = "Recuerda que la contraseña es de 8 o mas caracteres";
      return false;
    }


  }

