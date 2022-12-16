
$(function(){

	$('#select-depto').on('change', onSelectDeptoChange);

});


function onSelectDeptoChange(){

	var depto_id = $(this).val();
	

	

		if(! depto_id)
		{

		$('#select-distrito').html('<option value=""required>Seleccione Distrito</option>');
		return;
		}

//ajax
	$.get('/fichas/create/'+depto_id+'/distrito', function(datos1)
	{

		//console.log(datos);

		var html_select = '<option value=""required>Seleccione Distrito</option>';
		

		//console.log(datos.length);

		for (var i=0; i<datos1.length; ++i)
			html_select += '<option value="'+datos1[i].id+'">'+datos1[i].name+'</option>';




		$('#select-distrito').html(html_select);
	})

}
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
$(function(){

	$('#identidad_de_genero').on('change', onSelectGeneroChange);

});


function onSelectGeneroChange(){

	var generos_id = $(this).val();


		if(! generos_id)
		{

		$('#sub_identidad_de_genero').html('<option value=""required>Seleccione...</option>');
		return;
		}
	

	
//ajax
	$.get('/fichas/create/'+generos_id+'/subgenero', function(datos3)
	{

		
		var html_select = '<option value=""required>Seleccione...</option>';


		

		for (var i=0; i<datos3.length; ++i)
			html_select += '<option value="'+datos3[i].id+'">'+datos3[i].name+'</option>';




		$('#sub_identidad_de_genero').html(html_select);



	})

}

/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$(function(){

	$('#discriminafamilia').on('change', onSelectDfliaChange);

});


function onSelectDfliaChange(){

	var dflia_id = $(this).val();


		if(! dflia_id)
		{

		$('#subdiscriminafamilia').html('<option value="">Seleccione...</option>');
		return;
		}
	
//ajax
	$.get('/fichas/create/'+dflia_id+'/subdflia', function(datos2)
	{

		
		var html_select = '<option value="">Seleccione...</option>';


	
		for (var i=0; i<datos2.length; ++i)
			html_select += '<option value="'+datos2[i].id+'">'+datos2[i].name+'</option>';




		$('#subdiscriminafamilia').html(html_select);



	})

}

/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$(function(){

  $('.validanumericos').keypress(function(e) {
    if(isNaN(this.value + String.fromCharCode(e.charCode))) 
     return false;
  })
  .on("cut copy paste",function(e){
    e.preventDefault();
  });

});
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#controlesperiodicos").change( function() {
        if ($(this).val() === "SI") {
            $("#controlesperiodicos_pq").prop("disabled", false);
        } else {
            $("#controlesperiodicos_pq").prop("disabled", true);
        }
    });
});
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#tienedondevivir").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#vivienda_tenencia").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#vivienda_tenencia").prop("disabled", true);
        	}

        else {
            $("#vivienda_tenencia").prop("disabled", false);
        	}

    });
});

/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#obra_social").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#obrasocialnombre").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#obrasocialnombre").prop("disabled", true);
        	}

        else {
            $("#obrasocialnombre").prop("disabled", false);
        	}

    });
});
  
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#medicacionpermanente").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#medicacionlugar").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#medicacionlugar").prop("disabled", true);
        	}

        else {
            $("#medicacionlugar").prop("disabled", false);
        	}

    });
});

/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#hormonasgratis").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#hormonasdonde").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#hormonasdonde").prop("disabled", true);
        	}

        else {
            $("#hormonasdonde").prop("disabled", false);
        	}

    });
});
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#discrimina").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#discrimina_donde").prop("disabled", true);
            $("#discrimina_donde1").prop("disabled", true);
            $("#discrimina_donde2").prop("disabled", true);
            $("#discrimina_donde3").prop("disabled", true);
            $("#discrimina_donde4").prop("disabled", true);
            $("#discrimina_donde5").prop("disabled", true);
            $("#discrimina_donde6").prop("disabled", true);
            $("#discrimina_donde7").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#discrimina_donde").prop("disabled", true);
            $("#discrimina_donde1").prop("disabled", true);
            $("#discrimina_donde2").prop("disabled", true);
            $("#discrimina_donde3").prop("disabled", true);
            $("#discrimina_donde4").prop("disabled", true);
            $("#discrimina_donde5").prop("disabled", true);
            $("#discrimina_donde6").prop("disabled", true);
            $("#discrimina_donde7").prop("disabled", true);
        	}

        else {
            $("#discrimina_donde").prop("disabled", false);
            $("#discrimina_donde1").prop("disabled", false);
            $("#discrimina_donde2").prop("disabled", false);
            $("#discrimina_donde3").prop("disabled", false);
            $("#discrimina_donde4").prop("disabled", false);
            $("#discrimina_donde5").prop("disabled", false);
            $("#discrimina_donde6").prop("disabled", false);
            $("#discrimina_donde7").prop("disabled", false);
        	}

    });
});




 /*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#discriminasalud").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#discriminasalud_donde").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#discriminasalud_donde").prop("disabled", true);
        	}

        else {
            $("#discriminasalud_donde").prop("disabled", false);
        	}

    });
});
 /*---------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#discriminaeducacion").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#discriminaeducacion_donde").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#discriminaeducacion_donde").prop("disabled", true);
        	}

        else {
            $("#discriminaeducacion_donde").prop("disabled", false);
        	}

    });
});

 /*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#discriminaeducacion").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#discriminaeducacion_donde").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#discriminaeducacion_donde").prop("disabled", true);
        	}

        else {
            $("#discriminaeducacion_donde").prop("disabled", false);
        	}

    });
});

 /*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#discriminatrabajo").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#discriminatrabajo_donde").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#discriminatrabajo_donde").prop("disabled", true);
        	}

        else {
            $("#discriminatrabajo_donde").prop("disabled", false);
        	}

    });
});
 /*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#capacitacionedu").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#capacitacioneducual").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#capacitacioneducual").prop("disabled", true);
        	}

        else {
            $("#capacitacioneducual").prop("disabled", false);
        	}

    });
});
 /*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#discapacidad").change( function() {
        if ($(this).val() === "NO" ) 
        	{
            $("#cud").prop("disabled", true);
             $("#tipo_discapacidad").prop("disabled", true);
        	}
		else if ($(this).val() === "NC") {
            $("#cud").prop("disabled", true);
            $("#tipo_discapacidad").prop("disabled", true);
        	}

        else {
            $("#cud").prop("disabled", false);
            $("#tipo_discapacidad").prop("disabled", false);
        	}

    });
});

 /*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/

$( function() {
    $("#condicionlaboral").change( function() {
        if ($(this).val() === "NC" ) 
        	{
            $("#cat_ocupacional").prop("disabled", true);
            $("#capacitacionedu").prop("disabled", true);
            $("#catinactividad").prop("disabled", true);
             
        	}
			else if ($(this).val() === "Desocupada/o/e") {
            $("#cat_ocupacional").prop("disabled", false);
            $("#capacitacionedu").prop("disabled", false);
            $("#catinactividad").prop("disabled", true);
        	}
        
        	else if ($(this).val() === "Inactiva/o/e") {
           $("#catinactividad").prop("disabled", false);
            $("#cat_ocupacional").prop("disabled", true);
            $("#capacitacionedu").prop("disabled", true);
        	}

        else {
            $("#cat_ocupacional").prop("disabled", false);
            $("#catinactividad").prop("disabled", true);
            $("#capacitacionedu").prop("disabled", false);
        	}

    });
});

 /*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/


