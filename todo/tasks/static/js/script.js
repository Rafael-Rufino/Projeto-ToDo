// criando uma função em jquery para monstar uma alerta ao usuairo antes de apapar a tarefa

$(document).ready(function(){
    var deleteBtn = $('.delete-btn');

    $(deleteBtn).on('click', function(e){
        e.preventDefault();
        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        // se o usuario digitar ok a tarefa é apagada
        if(result){
            window.location.href = delLink;
        }
    });
});