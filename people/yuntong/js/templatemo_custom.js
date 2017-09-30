jQuery(document).ready(function($) {

	$(".main-menu a").click(function(){
		var id =  $(this).attr('class');
		id = id.split('-');
		$('a.active').removeClass('active');

    	$(this).addClass('active');
		$("#menu-container .content").slideUp('slow');
		$("#menu-container #menu-"+id[1]).slideDown('slow');		
		$("#menu-container .homepage").slideUp('slow');
		return false;
	});


	$(".main-menu a.homebutton").click(function(){
		$("#menu-container .content").slideUp('slow');
		$("#menu-container .homepage").slideDown('slow');
		return false;
	});

	$(".main-menu a.aboutbutton").click(function(){
		$("#menu-container .content").slideUp('slow');
		$("#menu-container .about-section").slideDown('slow');
		return false;
	});

	$(".main-menu a.biographybutton").click(function(){
		$("#menu-container .content").slideUp('slow');
		$("#menu-container .biography-section").slideDown('slow');
		return false;
	});

	$(".main-menu a.experiencesbutton").click(function(){
		$("#menu-container .content").slideUp('slow');
		$("#menu-container .experiences-section").slideDown('slow');
		return false;
	});

	$(".main-menu a.publicationsbutton").click(function(){
		$("#menu-container .content").fadeOut();
		$("#menu-container .publications-section").slideDown('slow');
		//loadScript();
		return false;
	});

        $(".main-container a.aboutbutton").click(function(){
        $("#menu-container .homepage").slideUp('slow');
		$("#menu-container .content").slideUp('slow');
		$("#menu-container .about-section").slideDown('slow');
		return false;
	});

	$(".main-container a.biographybutton").click(function(){
        $("#menu-container .homepage").slideUp('slow');
		$("#menu-container .content").slideUp('slow');
		$("#menu-container .biography-section").slideDown('slow');
		return false;
	});

	$(".main-container a.experiencesbutton").click(function(){
        $("#menu-container .homepage").slideUp('slow');
		$("#menu-container .content").slideUp('slow');
		$("#menu-container .experiences-section").slideDown('slow');
		return false;
	});

	$(".main-container a.publicationsbutton").click(function(){
        $("#menu-container .homepage").slideUp('slow');
		$("#menu-container .content").fadeOut();
		$("#menu-container .publications-section").slideDown('slow');
		//loadScript();
		return false;
	});



	$('a.toggle-nav').click(function(){
		$('.menu-responsive').slideToggle();
	});

	$('.menu-responsive a').click(function() {
		$('.menu-responsive').slideToggle().hide();
	});




});


function loadScript() {
	  var script = document.createElement('script');
	  script.type = 'text/javascript';
	  script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&' +
	      'callback=initialize';
	  document.body.appendChild(script);
	}

	function initialize() {
	    var mapOptions = {
	      zoom: 15,
	      center: new google.maps.LatLng(16.8496189,96.1288854)
	    };
	    var map = new google.maps.Map(document.getElementById('map_canvas'),  mapOptions);
	}