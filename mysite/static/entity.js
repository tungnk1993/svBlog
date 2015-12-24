$(function() {
	console.log("entity.js loaded");

	handle_vote_change();
	handle_delete_review();
})

function handle_vote_change() {

	$(".vote-btn").on("click", function(e) {
		e.preventDefault();
		var vote_review_id = $(this).attr("review-id");
		var vote_value = parseInt($(this).attr("vote-value"));
		var this_is_on = $(this).hasClass("btn-primary") || $(this).hasClass("btn-danger");

		console.log("Clicked", vote_review_id, vote_value, this_is_on);

		var other_button = $("button[review-id="+vote_review_id+"][vote-value="+(1-vote_value)+"]");
		var other_is_on = $(other_button).hasClass("btn-primary") || $(other_button).hasClass("btn-danger");

		console.log("Other ", other_is_on);
		var ajax_vote_value = -1;
		var delta_up = 0, delta_total = 0;
		if (!(this_is_on || other_is_on))
		{
			// both button not voted
			ajax_vote_value = vote_value;
			delta_total++;
			delta_up = vote_value;
			console.log("AJAX VOTE ", vote_review_id, vote_value);
			if (vote_value == 1) $(this).addClass("btn-primary");
			else $(this).addClass("btn-danger");
			$(this).removeClass("btn-default-my");
		}
		else
		{
			// one button is voted
			if (this_is_on)
			{
				// cancel the vote
				ajax_vote_value = 2;
				delta_total--;
				delta_up = -vote_value;
				console.log("AJAX VOTE ", vote_review_id, 2);
				if (vote_value == 1) $(this).removeClass("btn-primary");
				else $(this).removeClass("btn-danger");
				$(this).addClass("btn-default-my");
			}
			else
			{
				// toggle the vote
				ajax_vote_value = vote_value;
				if (vote_value == 0) delta_up = - 1;
				else delta_up = 1;
				console.log("AJAX VOTE ", vote_review_id, vote_value);
				$(other_button).removeClass("btn-primary");
				$(other_button).removeClass("btn-danger");
				$(other_button).addClass("btn-default-my");
				if (vote_value == 1) $(this).addClass("btn-primary");
				else $(this).addClass("btn-danger");
				$(this).removeClass("btn-default-my");
			}
		}
		$(this).blur();

		// fake calculation
		var vote_info = $("h6[review-id-info="+vote_review_id+"]").children();
		var vote_up = parseInt(vote_info.eq(0).text());
		var vote_total = parseInt(vote_info.eq(1).text());
		var vote_percent = parseInt(vote_info.eq(2).text());
		console.log(vote_up, vote_total, vote_percent);

		vote_up += delta_up;
		vote_total += delta_total;
		if (vote_total == 0) vote_percent = 0;
		else
		{
			vote_percent = Math.floor(100.0 * vote_up / vote_total);
		}
		console.log(vote_up, vote_total, vote_percent);
		vote_info.eq(0).text(vote_up);
		vote_info.eq(1).text(vote_total);
		vote_info.eq(2).text(vote_percent);
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