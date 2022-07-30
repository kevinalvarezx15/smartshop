var tblSale;

$(function () {

    tblSale = $('#example').DataTable({

        language: {
            "select": {
            "cells": {
                "1": "",
                "_": ""
            },
            "columns": {
                "1": "",
                "_": ""
            },
            "rows": {
                "1": "",
                "_": ""
            }
            },
            "processing": "Procesando...",
            "lengthMenu": "Mostrar _MENU_ registros",
            "zeroRecords": "No se encontraron resultados",
            "emptyTable": "Ningún dato disponible en esta tabla",
            "infoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "infoFiltered": "(filtrado de un total de _MAX_ registros)",
            "search": "Buscar:",
            "infoThousands": ",",
            "loadingRecords": "Cargando...",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sortDescending": ": Activar para ordenar la columna de manera descendente"
            },
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros"
            
        },
        "dom": '<"toolbar">frtip',
        select: {
            style: 'single'
        },
        searching: true,
        responsive: true,
        "scrollX": true,
        scrollY:        '50vh',
        scrollCollapse: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata',
                
            },
            dataSrc: ""
        },
        columns: [
            {"data": "Compra_Id"},
            {"data": "proveedor"},
            {"data": "fechaCompra"},
            {"data": "total"},
            {"data": "estadoCompra"},
            {"data": "Compra_Id"},

        ],
        columnDefs: [
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '$' + parseFloat(data).toFixed(2);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    //var buttons = '<a href="/erp/sale/delete/' + row.Compra_Id + '/" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    var buttons = '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="bi bi-zoom-in"></i></a> ';
                    //var buttons = '<a href="/erp/sale/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });


    //Model
    $('#example tbody')
    .on('click', 'a[rel="details"]', function () {
        var tr = tblSale.cell($(this).closest('td, li')).index();
        var data = tblSale.row(tr.row).data();
        console.log(data);

        $('#tblDet').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            language: {
                "select": {
                "cells": {
                    "1": "",
                    "_": ""
                },
                "columns": {
                    "1": "",
                    "_": ""
                },
                "rows": {
                    "1": "",
                    "_": ""
                }
                },
                "processing": "Procesando...",
                "lengthMenu": "Mostrar _MENU_ registros",
                "zeroRecords": "No se encontraron resultados",
                "emptyTable": "Ningún dato disponible en esta tabla",
                "infoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
                "infoFiltered": "(filtrado de un total de _MAX_ registros)",
                "search": "Buscar:",
                "infoThousands": ",",
                "loadingRecords": "Cargando...",
                "paginate": {
                    "first": "Primero",
                    "last": "Último",
                    "next": "Siguiente",
                    "previous": "Anterior"
                },
                "aria": {
                    "sortAscending": ": Activar para ordenar la columna de manera ascendente",
                    "sortDescending": ": Activar para ordenar la columna de manera descendente"
                },
                "info": "Mostrando _START_ a _END_ de _TOTAL_ registros"
                
            },
            select: {
                style: 'single'
            },
            searching: true,
            responsive: true,
            "scrollX": true,
            scrollY:        '50vh',
            scrollCollapse: true,
            //data: data.det,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_details_prod',
                    'Compra_Id': data.Compra_Id
                },
                dataSrc: ""
            },
            columns: [
                {"data": "producto.nombre"},
                {"data": "producto.tipoProducto.nombre"},
                {"data": "precioCompra"},
                {"data": "cantidad"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [-1, -3],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return data;
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });

        $('#myModelDet').modal('show');
    });
    
});
