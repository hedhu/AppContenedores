let dataTable;
let dataTableIsInitialized = false;

const initDataTable = async() => {
    if(dataTableIsInitialized) {
        dataTable.destroy();
    }

    dataTable = new DataTable('#datatable_contenedores', {
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        },
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