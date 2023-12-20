function initMap() {
    var latitudText = document.getElementById('latitud').innerText.replace(',', '.');
    var longitudText = document.getElementById('longitud').innerText.replace(',', '.');

    var latitud = parseFloat(latitudText);
    var longitud = parseFloat(longitudText);

    var center = new google.maps.LatLng(latitud, longitud);

    var mapOptions = {
        center: center,
        zoom: 8, 
    };

    var map = new google.maps.Map(document.getElementById('map'), mapOptions);

    var marker = new google.maps.Marker({
        position: center,
        map: map,
        title: 'Ubicación Actual'
    });
}    

document.addEventListener('DOMContentLoaded', function () {
    var mostrarMapaBtn = document.getElementById('mostrarMapaBtn');
    var cerrarMapaBtn = document.getElementById('cerrarMapaBtn');

    mostrarMapaBtn.addEventListener('click', function () {
        initMap();
        document.getElementById('map').classList.remove('d-none');
        document.getElementById('map').classList.add('d-block');
        mostrarMapaBtn.disabled = true;
        cerrarMapaBtn.classList.remove('d-none');
    });

    cerrarMapaBtn.addEventListener('click', function () {
        document.getElementById('map').classList.remove('d-block');
        document.getElementById('map').classList.add('d-none');
        mostrarMapaBtn.disabled = false;
        cerrarMapaBtn.classList.add('d-none');
    });
});

function cerrarMapa() {
    var map = document.getElementById('map');
    map.classList.remove('d-block');
    map.classList.add('d-none');

    var mostrarMapaBtn = document.getElementById('mostrarMapaBtn');
    mostrarMapaBtn.disabled = false;

    var cerrarMapaBtn = document.getElementById('cerrarMapaBtn');
    cerrarMapaBtn.classList.add('d-none');
}
