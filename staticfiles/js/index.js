// form vailidation.
function validateForm() {
    // name validation
    var nameInput = document.getElementById("Name");
    var nameError = document.getElementById("nameLabel");
    var nameRegex = /^[a-zA-Z\s]+$/;
    if (!nameRegex.test(nameInput.value.trim())) {
        nameError.textContent = "Name must contain only letters!";
        return false;
    }else{
      nameError.textContent = "";
    }

    // phone validation
    var phoneInput = document.getElementById("phone");
    var phoneError = document.getElementById("phoneErr");
    var phoneRegex = /^[6789]?\d{9}$/;
    

    if (!phoneRegex.test(phoneInput.value)) {
        phoneError.textContent = "Please enter a valid phone number (xxx-xxx-xxxx)";
        return false;
    }else{
      phoneError.textContent = "";
    }
    // document.getElementById('submitted_msg').innerHTML = "Your record has been submitted"
return true;
}

// function for showing current System time
function showTime(){
    var date = new Date();
    var h = date.getHours();
    var m = date.getMinutes();
    var s = date.getSeconds();
    var session = "AM";
    if(h>=12){
      session = "PM";
    }
    if(h>12){
      h-=12;
    }
    h = h < 10? '0'+h : h;
    m = m < 10? '0'+m : m;
    s = s < 10? '0'+s : s;
    var T = h + "h : " + m + "m : " + s + "s "+session;
    document.getElementById('showTime').innerText = T;
    setInterval(showTime,1000);
   }