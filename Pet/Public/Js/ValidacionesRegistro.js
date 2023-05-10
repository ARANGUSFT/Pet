function validateForm() {
    // Reset error messages
    document.getElementById("usernameError").textContent = "";
    document.getElementById("emailError").textContent = "";
    document.getElementById("passwordError").textContent = "";
    

    // Get form values
    var username = document.forms["registrationForm"]["username"].value;
    var email = document.forms["registrationForm"]["email"].value;
    var password = document.forms["registrationForm"]["password"].value;
    

    // Validate username
    if (username === "") {
      document.getElementById("usernameError").textContent = "Por favor, ingresa un nombre de usuario.";
      return false;
    } else if (username.length < 4) {
      document.getElementById("usernameError").textContent = "El nombre de usuario debe tener minimo 4 y maximo 16 caracteres.";
      return false;
    } 
    

    // Validate email
    if (email === "") {
      document.getElementById("emailError").textContent = "Por favor, ingresa un correo electrónico.";
      return false;
    } else if (!validateEmail(email)) {
      document.getElementById("emailError").textContent = "Por favor, ingresa un correo electrónico válido.";
      return false;
    }

    // Validate password
    if (password === "") {
      document.getElementById("passwordError").textContent = "Por favor, ingresa una contraseña.";
      return false;
    } else if (password.length < 8) {
      document.getElementById("passwordError").textContent = "La contraseña debe tener al menos 8 caracteres y maximo 16";
      return false;
    }


  }

  function validateEmail(email) {
    // Simple email validation using regular expression
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
  }