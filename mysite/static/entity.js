$(function() {
	console.log("entity.js loaded");
	handle_vote_change();
	handle_delete_review();
})

function handle_vote_change() {

	$(".vote-btn").on("click", function(e) {
		e.preventDefault();
		var vote_review_id = $(this).attr("review-id");
		var this_is_on = $(this).hasClass("btn-pink");

		console.log("Clicked", vote_review_id, this_is_on);

		var ajax_vote_value, delta;
		if (this_is_on)
		{
			// turn off
			ajax_vote_value = 0;
			delta = -1;
			console.log("AJAX VOTE ", vote_review_id, ajax_vote_value);
			$(this).removeClass("btn-pink");
			$(this).addClass("btn-default-my");
			$(this).next().removeClass("btn-pink");
			$(this).next().removeClass("btn-left-border");
			$(this).next().addClass("btn-default-my");
		}
		else
		{
			// turn on
			ajax_vote_value = 1;
			delta = 1;
			console.log("AJAX VOTE ", vote_review_id, ajax_vote_value);
			$(this).removeClass("btn-default-my");
			$(this).addClass("btn-pink");
			$(this).next().removeClass("btn-default-my");
			$(this).next().addClass("btn-pink");
			$(this).next().addClass("btn-left-border");
			
		}
		$(this).blur();

		// fake calculation
		var vote_info = $(this).next();
		var new_value = parseInt(vote_info.html()) + delta;
		vote_info.html(new_value);

		// send ajax
		var url = "/vote/" + vote_review_id + "/" + ajax_vote_value + "/";
		console.log("Call ajax ", url);
		$.ajax({
			url: url,
			type: "GET",
			success: function(result) {
				console.log(result);
			}
		});
	})
}

function handle_delete_review()
{
	$('#delete-review').click(function() {
		bootbox.dialog({
		  message: "Bạn chắc muốn xóa đánh giá chứ?",
		  title: "Bình tĩnh!",
		  buttons: {
			
			danger: {
			  label: "Yes!",
			  className: "btn-danger",
			  callback: function() {
				var url = window.location.href + "delete-review/";
				console.log("Call ajax ", url);
				$.ajax({
					url: url,
					type: "GET",
					success: function(result) {
						location.reload();
					},
					error: function (request, error) {
						console.log(error);
					}
				});
			  }
			},
			main: {
			  label: "Cancel",
			  className: "btn-default",
			  callback: function() {
				console.log("Delete cancel");
			  }
			}
		  }
		});
	});
}