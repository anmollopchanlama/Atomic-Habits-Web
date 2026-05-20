alert(`YOU DO NOT RISE TO THE LEVEL OF YOUR GOALS. \n
YOU FALL TO THE LEVEL OF YOUR SYSTEMS.  \n
                             !!!WELCOME!!!`)


function navToAboutUs() {

    window.location.href = "aboutus.html";

}

function navToSocials() {
    window.location.href = "socials.html";
}


function navToContactUs() {
    window.location.href = "contact.html";
}


const title = document.getElementById ("hey");
console.log(title);

title.addEventListener("click", function() {
    title.style.color = "blue";
    title.innerText = "You clicked me!"; });

function change(){

    let data   =  document.querySelectorAll(".text");
    data[2].textContent = "This is a new simple document3"
    data[1].innerHTML='<input type="password">';
}

function reset() {
    // 1. Fixed the ID selector: added quotes and removed the #
    let resetBtn = document.getElementById("reset");

    // 2. Set the click "trigger" directly
    resetBtn.onclick = function() {
        // 3. Change the color
        resetBtn.textContent = "HEYYYYYY";
        resetBtn.style.backgroundColor = "red";
        resetBtn.style.color = "white";
        
        
        console.log("Reset button clicked and color changed!");
    };
}

// Run the function so it sets up the 'trigger'
reset();

function change2() {

    let data = document.querySelectorAll(".text");
    data[1].textContent = "This is a new simple doument 3."
    data[ 1]



}

 


function submit() {
    // 1. Get Values
    let email = document.getElementById("email").value;
    let password = document.getElementById("pwd").value;
    let confirmPassword = document.getElementById("cpwd").value;
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    let isValid = true;

    // 2. Validate Email
    if (!emailRegex.test(email)) {
        showError("email", "Please enter a valid email.");
        isValid = false;
    } else {
        showSuccess("email");
    }

    // 3. Validate Password Length
    if (password.length < 6) {
        showError("pwd", "Password length is not enough.");
        isValid = false;
    } else {
        showSuccess("pwd");
    }

    // 4. Validate Match
    if (confirmPassword === "") {
        showError("cpwd", "Please confirm your password.");
        isValid = false;
    } else if (password !== confirmPassword) {
        showError("cpwd", "Passwords do not match.");
        isValid = false;
    } else {
        showSuccess("cpwd");
    }

    if (isValid) {
        alert("Form submitted successfully!");
    }
}



function showError(inputId, message) {
    const input = document.getElementById(inputId);
    const error = document.getElementById(inputId + "-error");
    input.classList.add("input-error");
    error.textContent = message;
    error.style.display = "block";
    error.style.color = "red";
}

function showSuccess(inputId) {
    const input = document.getElementById(inputId);
    const error = document.getElementById(inputId + "-error");
    input.classList.remove("input-error");
    input.classList.add("input-success");
    error.textContent = "";
    error.style.display = "none";
}



fucction validdate() { 

    let emailValidate = dopcument.getlementById("email").value;
    if (!validateEmail(email))
}