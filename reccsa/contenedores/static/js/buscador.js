let dataTable;
let dataTableIsInitialized = false;

const initDataTable = async() => {
    if(dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listContenedores();

    dataTable = new DataTable('#datatable_contenedores', {});
    dataTableIsInitialized=true;
}

const listContenedores = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/contenedores/list_contenedores/');
        const data = await response.json();

        let content = '';
        data.contenedores.forEach((contenedor, index) => {
            const facturaCorrespondiente = data.facturas.find(factura => factura.U_CONTAINER === contenedor.codigo);

            content +=`
                <tr>
                    <td class='text-center'>${contenedor.codigo}</td>
                    <td class='text-center'>${facturaCorrespondiente ? facturaCorrespondiente.DocNum : '-'}</td>
                    <td class='text-center'>${contenedor.estado}</td>
                    <td class='text-center'>${contenedor.ultima_actualizacion_tracking}</td>
                    <td class='text-center'>${contenedor.ultima_actualizacion_tracking}</td>
                </tr>
            `
        });
        tableBody_contenedores.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener('load', async () => {
    await initDataTable();
})