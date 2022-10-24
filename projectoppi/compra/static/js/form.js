var tblProductos;
var compras = {
    items: {
        proveedor: '',
        fechaCompra: '',
        total: 0.00,
        estadoCompra: '',
        productos: []
    },
    calculate_invoice: function () {
        var subtotal = 0.00;
        $.each(this.items.productos, function (pos, dict) {
            dict.pos = pos;
            dict.subtotal = dict.cantidad * parseFloat(dict.precio_compra);
            subtotal += dict.subtotal;
        });
        this.items.total = subtotal;

        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function (item) {
        this.items.productos.push(item);
        this.list();
    },
    list: function () {
        this.calculate_invoice();
        tblProductos = $('#tblProductos').DataTable({
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
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.productos,
            columns: [
                {"data": "id"},
                {"data": "nombre"},
                {"data": "tipoProducto.nombre"},
                {"data": "precio_compra"},
                {"data": "cantidad"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs bbtn-flat bi bi-x" style="color: white;"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" id name="precio_compra" onchange="setTwoNumberDecimal()" step="0.01" class="form-control currency" autocomplete="off" value="' + row.precio_compra + '">';
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cantidad" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cantidad + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cantidad"]').TouchSpin({
                    min: 1,
                    max: 1000000000,
                    step: 1
                });
                //$(row).find('input[name="precio_compra"]').TouchSpin({
                 //   min: 1,
                  //  stepinterval: 50,
                 ////   maxboostedstep: 10000000,
                  //  decimals: 2,
                 //   prefix: '$'
                //});
                

            },
            initComplete: function (settings, json) {

            }
        });
    },
};

function setTwoNumberDecimal(event) {
    $('input[name="precio_compra"]').val( parseFloat($('input[name="precio_compra"]').val()).toFixed(2));
    
}

$(function () {
    $('.select2').select2({
        language: 'es',
        theme: 'bootstrap4',
        dropdownParent: $('#edicion'),
        
    });

    $('#fechaCompra').datetimepicker({
        format: 'YYYY-MM-DD',
        
        locale: 'es'
        
        //minDate: moment().format("YYYY-MM-DD")
    });


    $('input[name="search"]').autocomplete({
        appendTo:$('#edicion'),
        source: function (request, response) {
            $.ajax({
                url: '/compra/Crear/',
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.precio_compra = 1000.00;
            ui.item.cantidad = 1;
            ui.item.subtotal = 0.00;
            console.log(compras.items);
            compras.add(ui.item);
            $(this).val('');
        }
    });
    $('.btnRemoveAll').on('click', function () {
        if (compras.items.productos.length === 0) return false;
        Swal.fire({
            title: 'Estas seguro?',
            text: "No podrás revertir esto!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            cancelButtonText:'Cancelar',
            confirmButtonText: 'Si, deseo eliminarlo!'
            }).then((result) => {
                compras.items.productos = [];
                compras.list();
            })       
    });
    $('#tblProductos tbody')

        .on('change', 'input[name="cantidad"]', function () {
            var cantidad = parseInt($(this).val());
            var tr = tblProductos.cell($(this).closest('td, li')).index();
            compras.items.productos[tr.row].cantidad = cantidad;
            compras.calculate_invoice();
            $('td:eq(5)', tblProductos.row(tr.row).node()).html('$' + compras.items.productos[tr.row].subtotal.toFixed(2));
            
        })
        .on('click', 'a[rel="remove"]', function () {
            console.log('1111111111')
            var tr = tblProductos.cell($(this).closest('td, li')).index();

            Swal.fire({
            title: 'Estas seguro?',
            text: "No podrás revertir esto!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            cancelButtonText:'Cancelar',
            confirmButtonText: 'Si, deseo eliminarlo!'
            }).then((result) => {
                if (result.isConfirmed) {
                    compras.items.productos.splice(tr.row, 1);
                    compras.list();
                }
            })
            
        })
        .on('change', 'input[name="precio_compra"]', function () {
            var precio_compra = parseInt($(this).val());
            var tr = tblProductos.cell($(this).closest('td, li')).index();
            compras.items.productos[tr.row].precio_compra = precio_compra;
            compras.calculate_invoice();
            $('td:eq(5)', tblProductos.row(tr.row).node()).html('$' + compras.items.productos[tr.row].precio_compra.toFixed(2));
            
        });
        

        
        $('form').on('submit', function(e){
            e.preventDefault();
            if(compras.items.productos.length === 0){
                message_error('Debe al menos tener un item en su detalle de venta');
                return false;
            }  
            compras.items.fechaCompra = $('input[name="fechaCompra"]').val();
            compras.items.proveedor = $('select[name="proveedor"]').val();
            compras.items.estadoCompra = $('select[name="estadoCompra"]').val();
            var parameters = new FormData();
            parameters.append('action', $('input[name="action"]').val());
            parameters.append('compras', JSON.stringify(compras.items));
            console.log('322222222')
            $.ajax({
              
              url:'/compra/Crear/',
              type:'POST',
              data: {
                'action': $('input[name="action"]').val(),
                'compras': JSON.stringify(compras.items)
                },
              dataType:'json'      
            }).done(function(data){
              if(!data.hasOwnProperty('error')){
                Swal.fire({
                  text:'El registro ha sido almacenado correctamente',
                  icon: 'success',
                  confirmButtonColor: '#3085d6',
                })
                window.location='/compra/';
                //location.href('/cliente/');
                // location.
                return false;
              }
              message_error(data.error);
        
            }).fail(function (jqXHR, textStatus, errorThrown) {
              alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {
            });
        });

    }) 
 
    

