document.addEventListener("DOMContentLoaded", function() {
    const logoImage = document.getElementById("logo");
    const linkLogo = document.getElementById("linkLogo");
    const logins = document.getElementsByClassName("log");

    if (logins.length > 0) {    
        if (logoImage) {
            for (const login of logins) {
                logoImage.classList.remove("w-25");
                logoImage.classList.add("w-100");
                login.classList.add("d-none");
            }
        }
    }

    if (linkLogo) {
        linkLogo.addEventListener("click", function(event) {
            event.preventDefault();
        });
    }
});