
$(document).ready(function() {

// ARRIVAL TIME – UPDATING
    $('#arrival-time').change(function(){
        var inputDate = this.value;
        $(this).attr("value", inputDate)
    });

// TOLERANCE – SLIDER 
	$( function() {
		$( "#slider-tolerance" ).slider({
			range: true,
			min: -60,
			max: 60,
			values: [ -30, 30 ],
			slide: function( event, ui ) {
				$( "#tolerance-min" ).val( ui.values[ 0 ] + "min" );
				$( "#tolerance-max" ).val( "+ " + ui.values[ 1 ] + "min" );
			}
		});
		$( "#tolerance-min" ).val( $( "#slider-tolerance" ).slider( "values", 0 ) + "min" );
		$( "#tolerance-max" ).val( "+" + $( "#slider-tolerance" ).slider( "values", 1 ) + "min" );
	});

// ACTIVE DAYS – TOGGLING
	$("#days li").click(function() {
		$(this).toggleClass("active");
	});



	$("#submit").click(function() {


		// collect the form data while iterating over the inputs
		function trip() {
			this.arr = $("#arrival-time").attr("value");
			this.org = $("#origin-location").val();
			this.dst = $("#destination-location").val();
			this.tolerance = [$("#tolerance-min").val(), $("#tolerance-max").val()];
			// this.activeDays = []
		};

		var data = new trip();

		console.log(data);
		// construct an HTTP request
		var xhr = new XMLHttpRequest();
		xhr.open("post", "localhost:5555/api/fastRoute", true);
		xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');

		// send the collected data as JSON
		xhr.send(JSON.stringify(data));

		xhr.onloadend = function () {
			// done
			console.log("done");
		};
	});


});
