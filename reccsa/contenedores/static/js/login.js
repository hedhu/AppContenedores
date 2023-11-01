// Cambiar la clase y el ancho de la imagen con id "logo"
document.addEventListener("DOMContentLoaded", function() {
    const logoImage = document.getElementById("logo");
    const linkLogo = document.getElementById("linkLogo");
    const login = document.getElementById("btnLogin");

    if (logoImage) {
        logoImage.classList.remove("w-25");
        logoImage.classList.add("w-100");
        login.classList.add("d-none");
    }

    if (linkLogo) {
        linkLogo.addEventListener("click", function(event) {
            event.preventDefault();
        });
    }
});