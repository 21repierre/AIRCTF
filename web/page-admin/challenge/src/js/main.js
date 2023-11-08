const form = document.getElementById("form")
const usernameInput = document.getElementById("username")
const passwordInput = document.getElementById("password")
const errorMsg = document.getElementById("error_msg")

function checkCredentials(){
    let username = document.forms["connection_form"]["username"].value
    let password = document.forms["connection_form"]["password"].value

    if(username == "CTF_@dmin" && password == "CTF_p@ssw0rd"){
        alert("Félicitations, le flag est AIRCTF{WEB_@dmin_c0nnecti0n_js}")
    }else{
        errorMsg.style.display = "block";
    }
}

usernameInput.addEventListener("input", hideError);
passwordInput.addEventListener("input", hideError);

function hideError(){
    errorMsg.style.display = "none";
}