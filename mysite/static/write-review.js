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
})