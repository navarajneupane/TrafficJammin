
$(document).ready(function() {

// ARRIVAL TIME – UPDATING
    $('#arrival-time').change(function(){
        var inputDate = this.value;
        $(this).attr("value", inputDate)
    });

// TOLERANCE – SLIDER 
	$( function() {
		$( "#slider-tolerance" ).slider({
			range: "min",
			value: 20,
			min: 5,
			max: 60,
			slide: function( event, ui ) {
				$( "#tolerance-max" ).val( ui.value );
			}
		});
		$( "#tolerance-max" ).val( $( "#slider-tolerance" ).slider( "value") );
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
			this.tolerance = parseInt($("#tolerance-max").val());
			// this.activeDays = []
		};

		var data = new trip();

		console.log(data);
		// construct an HTTP request
		var xhr = new XMLHttpRequest();
		xhr.open("post", "http://localhost:5555/api/fastRoute", true);
		xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');

		// send the collected data as JSON
		xhr.send(JSON.stringify(data));

		xhr.onloadend = function () {
			// done
		};
	});


});
