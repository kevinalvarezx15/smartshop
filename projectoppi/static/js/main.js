function cerrarModal(){
    $('#edicion').modal('hide');
}

function registrar(){

    $.ajax({
        data:$('#form_creacion').serialize(),
        url:$('#form_creacion').attr('action'),
        type:$('#form_creacion').attr('method'),
        success:function(response){
            console.log(response);
            cerrarModal();
        },
        error:function(error){
            console.log(error)
        }
    })
}

function message_error(obj){
    debugger
    var html='';
    console.log(obj)
    if(typeof (obj)=='object'){
        html='<ul style="text-align:left;">';
        $.each(obj, function (key,value){
            //html+='<li>'+key+': '+value+'</li>';
            html+='<li> '+value+'</li>';
        })
        html+='</ul>';
    }
    else{
         html='<p>'+obj+'</p>';
    }  
        
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error',
      })
}

