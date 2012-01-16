what_did_the_box_said=''

$(document).ready(function(){

// Overlay fading effect
	$('div#overlay')
	.css('opacity', 0.9)
	.hover(function() {
		$(this).fadeTo('fast',1)
	}, function() {
		setTimeout(function() {
			$('div#overlay').fadeTo('fast',0.9)
			},"150")
	});

// Back to Top helper
	$('<div></div>').attr('id','back-to-top')
	.html('<span>Go back to the top<br/><b>NOW<b></span>')
	.css('opacity', 0.5)
	.hover(function() {
		$(this).animate( {'height':'50'}, {duration:'fast', easing:'swing'})
		.fadeTo('fast',0.9);
	}, function() {
		setTimeout(function() {
				$('div#back-to-top').animate( {'height':'23'},
					{duration:'fast', easing:'swing'})
					.fadeTo('fast',0.5);				
			},"250")
	})
	.click(function() {
		$("html, body").animate({
			scrollTop: "0px"
		}, {
			duration: 400,
			easing: "swing"
		});
		return false;
	}).appendTo('body');

// Search Form
	what_did_the_box_said = $('form#search input#id_string').val()
	
	$('form#search input#id_string').addClass('fancy-text')

	$('form#search input#id_string').focus( function() {
		if($(this).val() == what_did_the_box_said)
			$(this).val('')		
		$(this).removeClass('fancy-text')
	}).blur( function() {
		if($(this).val() == '')		
			$(this).val(what_did_the_box_said)				
		$(this).addClass('fancy-text')
	})

// Comment Form
	$('input#id_name').val('What\'s your name?').addClass('fancy-text')
	$('input#id_email').val('lenny@localhost.com').addClass('fancy-text')
	$('input#id_url').val('blogmaker.wordpress.com').addClass('fancy-text')
	$('textarea#id_comment').val('I love this site!').addClass('fancy-text')

	$('input#id_name').focus( function() {
		if($(this).val() == 'What\'s your name?')
			$(this).val('')
		$(this).removeClass('fancy-text')
	}).blur( function() {
		if($(this).val() == '')		
			$(this).val('What\'s your name?')
		$(this).addClass('fancy-text')
	})

	$('input#id_email').focus( function() {
		if($(this).val() == 'lenny@localhost.com')
			$(this).val('')
		$(this).removeClass('fancy-text')
	}).blur( function() {
		if($(this).val() == '')		
			$(this).val('lenny@localhost.com')	
		$(this).addClass('fancy-text')	
	})

	$('input#id_url').focus( function() {
		if($(this).val() == 'blogmaker.wordpress.com')
			$(this).val('')
		$(this).removeClass('fancy-text')
	}).blur( function() {
		if($(this).val() == '')		
			$(this).val('blogmaker.wordpress.com')		
		$(this).addClass('fancy-text')
	})

	$('textarea#id_comment').focus( function() {
		if($(this).val() == 'I love this site!')
			$(this).val('')
		$(this).removeClass('fancy-text')
	}).blur( function() {
		if($(this).val() == '')		
			$(this).val('I love this site!')		
		$(this).addClass('fancy-text')
	})

// Odd Comment Background Color Change
	$('div.comment-body:odd').css('background-color','#EAEAEA')

// Login form
	$('div#i-own-this-blog')
		.css('height','23')
		.css('visibility','visible')
		.css('display','block')
		.css('opacity','0.2')
		.hover(function() {
			$(this).animate( {'height':'123'}, {duration:'fast', easing:'swing'})
			.fadeTo('fast',0.9);			
		}, function() {
			setTimeout(function() {
				$('div#i-own-this-blog').animate( {'height':'23'},
					{duration:'fast', easing:'swing'})
					.fadeTo('fast',0.5);				
			},"250")
		})
	
	$('form#login-form input#id_username').val('username').addClass('fancy-text')
	$('form#login-form input#id_password').val('password').addClass('fancy-text')

	$('input#id_username').focus( function() {
		if($(this).val() == 'username')
			$(this).val('')
		$(this).removeClass('fancy-text')
	}).blur( function() {
		if($(this).val() == '')		
			$(this).val('username')		
		$(this).addClass('fancy-text')
	})

	$('input#id_password').focus( function() {
		if($(this).val() == 'password')
			$(this).val('')
		$(this).removeClass('fancy-text')
	}).blur( function() {
		if($(this).val() == '')		
			$(this).val('password')		
		$(this).addClass('fancy-text')
	})

});