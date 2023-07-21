function validateForm() {
    var password = document.getElementById("password").value;
    var confPassword = document.getElementById("conf_password").value;
  
    if (password !== confPassword) {
      alert("Passwords do not match. Please re-enter your password.");
      return false;
    }
  
    return true;
  }
  