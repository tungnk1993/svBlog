$(function () {
  $('[data-toggle="popover"]').popover({
	container: 'body'
  });

  $('.rating-tooltip').rating({
	  extendSymbol: function (rate) {
		$(this).tooltip({
		  container: 'body',
		  placement: 'bottom',
		  title: 'Rate '
		});
	  }
	});

  var text_max = 100;
  var text_length = $('#review-content').val().length;
  var text_remaining = text_max - text_length;

  if (text_remaining <= 0) 
	$('#textarea-feedback').html("Đã đủ số kí tự tối thiểu :)");
  else
	$('#textarea-feedback').html("Cố lên, " + (text_max - text_length) + " kí tự nữa thôi!");

	$('#review-content').keyup(function() {
		var text_length = $('#review-content').val().length;
		var text_remaining = text_max - text_length;

		if (text_remaining <= 0) 
		{
			$('#textarea-feedback').html("Đã đủ số kí tự tối thiểu :)");
			$('#textarea-feedback').removeClass('text-danger');
		}
		else
		{
			$('#textarea-feedback').html("Cố lên, " + (text_max - text_length) + " kí tự nữa thôi!");
			$('#textarea-feedback').addClass('text-danger');
		}
	});

			
})