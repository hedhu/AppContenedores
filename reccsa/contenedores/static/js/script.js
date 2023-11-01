let containers;

// Load the JSON file
fetch('datacontenedor.json')
  .then(response => response.json())
  .then(data => {
    containers = Object.entries(data).map(([number, container]) => {
      container.data.metadata.number = number;
      return container;
    });
    populateContainerSelect();
  });

// Populate the container select with container numbers
function populateContainerSelect() {
  const containerSelect = document.getElementById('containerSelect');
  containers.forEach((container, index) => {
    const option = document.createElement('option');
    option.value = index;
    option.textContent = container.data.metadata.number;
    containerSelect.appendChild(option);
  });
}

// Display container data in the containerData div
function displayContainerData() {
  const containerSelect = document.getElementById('containerSelect');
  const selectedContainer = containers[containerSelect.value];
  showContainerData(selectedContainer);
}

// Search for a container by number and display it in the containerData div
function searchContainer() {
  const containerSearch = document.getElementById('containerSearch').value;
  const foundContainer = containers.find(container => container.data.metadata.number === containerSearch);
  if (foundContainer) {
    showContainerData(foundContainer);
  } else {
    document.getElementById('containerData').innerHTML = 'Container not found';
  }
}

// Show container data in the tables
function showContainerData(container) {
  document.querySelector("#metadata tbody").innerHTML = `
    <tr>
      
    <tr>
      <td>Number</td>
      <td>${container.data.metadata.number}</td>
    </tr>
    <tr>
      <td>Sealine Name</td>
      <td>${container.data.metadata.sealine_name}</td>
    </tr>
    <tr>
      <td>Status</td>
      <td>${container.data.metadata.status}</td>
    </tr>
    <tr>
      <td>Updated At</td>
      <td>${container.data.metadata.updated_at}</td>
    </tr>
  `;

  const locationsTable = document.querySelector("#locations thead");
  locationsTable.innerHTML = `
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>State</th>
      <th>Country</th>
    </tr>
  `;
  const locationsTBody = document.querySelector("#locations tbody");
  locationsTBody.innerHTML = "";
  container.data.locations.forEach(location => {
    locationsTBody.innerHTML += `
      <tr>
        <td>${location.id}</td>
        <td>${location.name}</td>
        <td>${location.state}</td>
        <td>${location.country}</td>
      </tr>
    `;
  });

// ################################################################
 

const facilityTable = document.querySelector("#facilities thead");
  facilityTable.innerHTML = `
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Country Code</th>
      
    </tr>
  `;
  const facilityTBody = document.querySelector("#facilities tbody");
  facilityTBody.innerHTML = "";
  container.data.facilities.forEach(location => {
    facilityTBody.innerHTML += `
      <tr>
        <td>${location.id}</td>
        <td>${location.name}</td>
        <td>${location.country_code}</td>
        
      </tr>
    `;
  });

  const pinTable = document.querySelector("#pin thead");
  pinTable.innerHTML = `
    <tr>
      <th>LON</th>
      <th>LAT</th>
    </tr>
  `;
  const pinTBody = document.querySelector("#pin tbody");
  pinTBody.innerHTML = "";
  const pinData = container.data.route_data.pin;
  pinTBody.innerHTML += `
    <tr>
      <td>${pinData[0]}</td>
      <td>${pinData[1]}</td>
    </tr>
  `;


  
  const containersTable = document.querySelector("#containers thead");
  containersTable.innerHTML = `
    <tr>
    <th>ORDER_ID</th>
    <th>NUMBER</th>
    <th>STATUS</th>
    <th>LOCATION</th>
    <th>FACILITY</th>
    <th>DESCRIPTION</th>
    <th>EVENT TYPE</th>
    <th>EVENT CODE</th>
    <th>STATUS</th>
    <th>DATE</th>
    <th>ACTUAL</th>
    <th>TYPE</th>
    <th>VESSEL</th>
    <th>VOYAGE</th>
    
    
    </tr>
  `;
  function getLocationNameById(id) {
    const foundLocation = container.data.locations.find(loc => loc.id === id);
    return foundLocation ? foundLocation.name : id;
  }
  
  function getFacilityNameById(id) {
    const foundFacility = container.data.facilities.find(fac => fac.id === id);
    return foundFacility ? foundFacility.name : id;
  } 

  const containersTBody = document.querySelector("#containers tbody");
  let rowsHTML = ""; // Usaremos una variable para almacenar todas las filas
  container.data.containers[0].events.forEach(event => {
    const locationName = getLocationNameById(event.location);
    const facilityName = getFacilityNameById(event.facility); // Obtenemos el nombre de la facility
    rowsHTML += `
      <tr>
        <td>${event.order_id}</td>
        <td>${container.data.containers[0].number}</td>
        <td>${container.data.containers[0].status}</td>
        <td>${locationName}</td>
        <td>${facilityName}</td> <!-- Usamos el nombre de la facility aquí -->
        <td>${event.description}</td>
        <td>${event.event_type}</td>
        <td>${event.event_code}</td>
        <td>${event.status}</td>
        <td>${event.date}</td>
        <td>${event.actual}</td>
        <td>${event.type}</td>
        <td>${event.vessel}</td>
        <td>${event.voyage}</td>
      </tr>
    `;
  });
  containersTBody.innerHTML = rowsHTML;

  // Navigate to the ruta.html page with pin data of the selected container
function navigateToRoute() {
  const containerSelect = document.getElementById('containerSelect');
  const selectedContainer = containers[containerSelect.value];
  const pinData = selectedContainer.data.route_data.pin;
  window.location.href = `ruta.html?lat=${pinData[0]}&lng=${pinData[1]}`;
}
}
