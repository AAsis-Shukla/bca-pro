function validatePassword() {

    // name validation
    var nameInput = document.getElementById("Name");
    var nameError = document.getElementById("nameError");
    var nameRegex = /^[a-zA-Z\s]+$/;
    if (!nameRegex.test(nameInput.value.trim())) {
        nameError.textContent = "Name must contain only letters";
        return false;
    }
    else{
        nameError.textContent = "";
    }

    // phone validation
    var phoneInput = document.getElementById("phone");
    var phoneError = document.getElementById("phoneErr");
    var phoneRegex = /^[6789]{1}\d{9}$/;
    // var phoneRegex = /^\d{3}-\d{3}-\d{4}$/;

    if (!phoneRegex.test(phoneInput.value)) {
        phoneError.textContent = "Please enter a valid phone number (xxx-xxx-xxxx)";
        return false;
    }else{phoneError.textContent = "";}

    // password validation
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;
    var errorMessage = document.getElementById("passwordErr");

    if (password !== confirmPassword) {
        errorMessage.textContent = "Passwords do not match!";
        return false;
    }
    else if (password.length < 8) {
        errorMessage.textContent = "Password must be at least 8 characters long";
        return false;
    }else{
        errorMessage.textContent = "";
    }

    return true;

}