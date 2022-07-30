

$(function () {

    $('#example').DataTable({

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
        initComplete: function (settings, json) {

        }
    });

});