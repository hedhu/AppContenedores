let dataTable;
let dataTableIsInitialized = false;

const initDataTable = async() => {
    if(dataTableIsInitialized) {
        dataTable.destroy();
    }

    dataTable = new DataTable('#datatable_contenedores', {
        searching: true, 
        columnDefs: [
            { targets: [2, 3, 4], searchable: false }, 
        ]
    });

    dataTableIsInitialized=true;
}
window.addEventListener('load', async () => {
    await initDataTable();
})