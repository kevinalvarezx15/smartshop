var tblProductos;
var ventas = {
    items: {
        cliente: '',
        fechaVenta: '',
        total: 0.00,
        estadoVenta: '',
        productos: []
    },
    calculate_invoice: function () {
        var subtotal = 0.00;
        $.each(this.items.productos, function (pos, dict) {
            dict.pos = pos;
            dict.subtotal = dict.cantidad * parseFloat(dict.precio_venta);
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
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.productos,
            columns: [
                {"data": "id"},
                {"data": "nombre"},
                {"data": "tipoProducto.nombre"},
                {"data": "precio_venta"},
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
                        return '$' + parseFloat(data).toFixed(2);
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
    $('input[name="precio_venta"]').val( parseFloat($('input[name="precio_venta"]').val()).toFixed(2));
    
}

$(function () {
    $('.select2').select2({
        language: 'es',
        theme: 'bootstrap4',
        dropdownParent: $('#edicion'),
        
    });

    $('#fechaVenta').datetimepicker({
        format: 'YYYY-MM-DD',
        
        locale: 'es'
        
        //minDate: moment().format("YYYY-MM-DD")
    });


    $('input[name="search"]').autocomplete({
        appendTo:$('#edicion'),
        source: function (request, response) {
            $.ajax({
                url: '/ventas/Crear/',
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
            ui.item.cantidad = 1;
            ui.item.subtotal = 0.00;
            console.log(ventas.items);
            ventas.add(ui.item);
            $(this).val('');
        }
    });
    $('.btnRemoveAll').on('click', function () {
        if (ventas.items.productos.length === 0) return false;
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
                ventas.items.productos = [];
                ventas.list();
            })       
    });
    $('#tblProductos tbody')

        .on('change', 'input[name="cantidad"]', function () {
            var cantidad = parseInt($(this).val());
            var tr = tblProductos.cell($(this).closest('td, li')).index();
            ventas.items.productos[tr.row].cantidad = cantidad;
            ventas.calculate_invoice();
            $('td:eq(5)', tblProductos.row(tr.row).node()).html('$' + ventas.items.productos[tr.row].subtotal.toFixed(2));
            
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
                    ventas.items.productos.splice(tr.row, 1);
                    ventas.list();
                }
            })
            
        })
        
        
        $('form').on('submit', function(e){
            e.preventDefault();
            if(ventas.items.productos.length === 0){
                message_error('Debe al menos tener un item en su detalle de venta');
                return false;
            }  
            ventas.items.fechaVenta = $('input[name="fechaVenta"]').val();
            ventas.items.cliente = $('select[name="cliente"]').val();
            ventas.items.estadoVenta = $('select[name="estadoVenta"]').val();
            var parameters = new FormData();
            parameters.append('action', $('input[name="action"]').val());
            parameters.append('ventas', JSON.stringify(ventas.items));
            console.log('322222222')
            $.ajax({
              
              url:'/ventas/Crear/',
              type:'POST',
              data: {
                'action': $('input[name="action"]').val(),
                'ventas': JSON.stringify(ventas.items)
                },
              dataType:'json'      
            }).done(function(data){
              if(!data.hasOwnProperty('error')){
                Swal.fire({
                  text:'El registro ha sido almacenado correctamente',
                  icon: 'success',
                  confirmButtonColor: '#3085d6',
                })
                window.location='/ventas/';
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
 
    

