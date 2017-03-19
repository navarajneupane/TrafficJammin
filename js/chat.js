
$(document).ready(function() {

	var newDate = {
		dst: "Eindhoven Station",
		ontime_org: "8:30",
		ontime_dst: "9:00",
		ontime_duration: 30,
		best_org: "8:15",
		best_dst: "8:35",
		best_duration: 20
	};

	var dst = newDate.dst,
		ontime_org = newDate.ontime_org,
		ontime_dst = newDate.ontime_dst,
		ontime_duration = newDate.ontime_duration,
		best_org = newDate.best_org,
		best_dst = newDate.best_dst,
		best_duration = newDate.best_duration,
		duration_ratio = 100 / ontime_duration * best_duration;

	setTimeout(function() {
		$(".chat-container").append('<p class="user small">Hey, what time shall I leave to reach ' + dst + ' around ' + ontime_dst + '?</p>');
	}, 1000);

	setTimeout(function() {
		$(".chat-container").append('<p class="bot small">You can do this:</p>')
	}, 3000);

	setTimeout(function() {
		$(".chat-container").append('<p class="bot small">Leave around ' +
		'<span id="ontime-org" class="suggest">' + ontime_org + '</span> to get there at ' +
		'<span id="ontime-dst" class="suggest">' + ontime_dst + '</span>' +
		'<br>' +
		'<span class="underline yellow-underline">' + ontime_duration + ' min</span></p>');
		setTimeout(function() {
			$(".yellow-underline").css("width", "100%");
		}, 100);
	}, 5000);

	setTimeout(function() {
		$(".chat-container").append('<p class="bot small">Or leave around ' +
		'<span id="best-org" class="suggest">' + best_org + '</span> to be there at '+
		'<span id="best-dst" class="suggest">' + best_dst + '</span> 😉'+
		'<br>' +
		'<span class="underline green-underline">' + best_duration + ' min</span></p>');
		setTimeout(function() {
			$(".green-underline").css("width", duration_ratio + "%");
		}, 100);
	}, 8000);

});
