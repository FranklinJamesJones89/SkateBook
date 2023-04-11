$(document).ready(function() {
});

spot_like_btn = document.getElementById('spot-like-btn');

spot_like_btn.addEventListener('click', function(event) {
	event.preventDefault();
	let targetUrl = spot_like_btn.getAttribute('href');
	window.location.href = targetUrl;
});


