let dataTable;
let dataTableIsInitialized = false;

const initDataTable = async() => {
    if(dataTableIsInitialized) {
        dataTable.destroy();
    }

    dataTable = new DataTable('#datatable_usuarios', {
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        },
        searching: true, 
        columnDefs: [
            { targets: [0, 3, 4, 5], searchable: false }, 
        ]
    });

    dataTableIsInitialized=true;
}
window.addEventListener('load', async () => {
    await initDataTable();
})