$(document).ready(function(){

/* anitmation */
	$('img').animate({  borderSpacing: -90 }, {
    step: function(now,fx) {
      $(this).css('-webkit-transform','rotate('+now+'deg)'); 
      $(this).css('-moz-transform','rotate('+now+'deg)');
      $(this).css('transform','rotate('+now+'deg)');
    },
    duration:'slow'
},'linear');

     
	$('.postBut').click(function(){
		var data = $('.theContent').val();
		var textArea = $('textarea');
		if ((data.length) != 0) {
		$('<li>').text(data).prependTo('.posts');
		$('li').css('color','#7B7B7B');
		textArea.val('');
		}
		else{
			alert('You have to write somethig for posting :) ');
		}
	});


});