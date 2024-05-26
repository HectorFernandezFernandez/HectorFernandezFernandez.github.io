$(document).ready(function(){

    $("#enviarCorreo").click(function(){
        function verificarDatos() {
            for (var campo in valoresGuardados) {
                if (valoresGuardados.hasOwnProperty(campo)) {
                    if (valoresGuardados[campo].trim() == '') {
                        return false;
                    }
                }
            }
            return true;
        }
        
        var todosLosDatosPresentes = verificarDatos();
        if(todosLosDatosPresentes){
            alert("Se ha enviado correo con exito")
        } else {
            alert("Faltan datos")
        }
        
    });

    verificarAnchoPantalla();

    $(window).resize(function(){
        verificarAnchoPantalla();
    });

    function verificarAnchoPantalla(){

        var anchoPantalla = $(window).width();
        
        var anchoMaximoTelefono = 768;

        if(anchoPantalla <= anchoMaximoTelefono){
            $("#quienesSomos").css("display","none");
            $("#carouselExampleControls").css("margin-top","-70px")
            $("#viajesChile").css("font-size","20px")
            $("#inicio").css("background","#000000")
        } else {
            $("#quienesSomos").css("display", "");
            $("#carouselExampleControls").css("margin-top","--72px")
            $("#viajesChile").css("font-size","")
            $("#inicio").css("background","")
        }
    }

});


    
