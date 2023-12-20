let dataTable;
let dataTableIsInitialized = false;

const initDataTable = async() => {
    if(dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listContenedores();

    dataTable = new DataTable('#datatable_contenedores', {
        searching: true, 
        columnDefs: [
            { targets: [0, 2, 3, 4], searchable: false }, 
        ]
    });

    dataTableIsInitialized=true;
}

const listContenedores = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/contenedores/list_contenedores/');
        const data = await response.json();

        let content = '';
        data.contenedores.forEach((contenedor, index) => {
            content +=`
                <tr>
                    <td class='text-center'>${contenedor.codigo}</td>
                    <td class='text-center'>${contenedor.doc_num || '-'}</td>
                    <td class='text-center'>${contenedor.estado}</td>
                    <td class='text-center'>${contenedor.ultima_actualizacion_tracking}</td>
                    <td class='text-center'>
                        <a href="${contenedor.url_contenedor}" class="detalles">
                            <i class="bi bi-arrow-right-circle"></i>
                        </a>
                    </td>
                </tr>
            `;
        });
        tableBody_contenedores.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener('load', async () => {
    await initDataTable();
})