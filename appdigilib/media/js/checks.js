$(document).ready(function() {

    $('.check_cat').change(function () {
        ajax_post_categorias();

    });


    $('.check_task').change(function () {
        ajax_post_tareas();
    });

    $('#Modal').on('shown.bs.modal', function (event) {
        id_article = event.relatedTarget.id;
        var modal = $(this);

        $.ajax({
            beforeSend: function (xhr, settings) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            type: 'POST',
            url: 'detail/',
            dataType: 'html',
            data: {
                'id_article': id_article,

            },
            success: function (response) {
                modal.find('.modal-body').html(response);

            },
            error: function (xhr, status, error) {
                alert("This article is not exist.");
            }
        });

    });
    //Disable "Enter" on keyboard
    $('#SearchForm').bind('keydown', function(e) {
        if (e.keyCode === 13) {
            e.preventDefault();
        }
    });

    $('#searchbutton').click(function f() {
        ajax_button_search();
    });

function getCookie(name) {

    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {

        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }

    }

    return cookieValue;
}

async function ajax_post_tareas(){
     var lista_task = [];
        $( '.check_task' ).each(function( index ) {
            if(this.checked) {
                lista_task.push($(this).attr('name'));
            }
            else{

            }
        });
        //var csrf;
        $.ajax({
            beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                type:'POST',
                url:'index/c2',
                dataType: 'html',
                data: {
                'lista': lista_task,
                },
            success: function(json){
              $('#content1').html(json);
            },
            error: function(xhr, status, error) {
                alert("error");
            }
        });
    }

async function ajax_post_categorias() {
    var list_marcados = [];
        $( '.check_cat' ).each(function( index ) {
            if(this.checked) {
                list_marcados.push($(this).attr('name'));

            }
            else{
                //lista_cat_des.push($(this).attr('name'));

            }
        });
        //var csrf;
        $.ajax({
            beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          },
            type:'POST',
            url:'index/c1',
            dataType:'html',
            data: {
                'lista': list_marcados,
            },
            success: function(json){
                $('#content1').html(json);
            },
            error: function(xhr, status, error) {
                alert("error");
            }
        });

    }

async function ajax_button_search() {
    let my_form = $('#searchInput').val();

     var lista_task_buscar = [];
     $( '.check_task' ).each(function( index ) {
         if(this.checked) {
             lista_task_buscar.push($(this).attr('name'));}
         else{}
     });

     var lista_cat_buscar = [];
     $( '.check_cat' ).each(function( index ) {
        if(this.checked) {
            lista_cat_buscar.push($(this).attr('name')); }
        else{}
     });

     var datos = {
         'list_task_search': lista_task_buscar,
         'list_cat_search': lista_cat_buscar,
         'my_form': my_form,
     };
     $.ajax({
         type:'POST',
         url:'',
         dataType:'html',
         data: datos,
         beforeSend: function(xhr, settings) {
                    var csrftoken = getCookie('csrftoken');
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);

                    },
         success: function(json){
             $('#content1').html(json);
         },
         error: function(xhr, status, error) {
             alert("error");
         }
        });

};

//Auxiliary Function to test button
function enviar() {
    var msj = "¿Tas?";
    alert(msj);
}

});

