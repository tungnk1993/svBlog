# svBlog

## Landing Page UI improve

* Slogan, take action
* Mission
* Make list teacher/uni more recognization

## Rating Page UI improve

* Make log-in more recognizable
* Add report option
* ~~Add function to insert/modify/suggest profile pic~~
* ~~Add share button~~
* Adjust spacing for review display
* Use mobile design

## TODO (should be in order)
* Small UI Fixes
	* Write_review_mobile
		* ~~Bigger star on write review mobile~~
		* Suggestion block
		* Countdown?
* Login notice when trying to vote
* Heart button under teacher image 
* Landing page (18-19)
* ~~Facebook sharing~~
	* Link URL to correct review
	* Teacher share
	* ~~Review share~~
* ~~Change voting to upvote only~~
	* ~~Update UI of vote~~
* Filter list of teacher/uni (20)
	* Name, subject, school first
* Modularize navbar, breakdown template
* COLOR COLOR COLOR
* Ipad Portrait mode problem.....

## Deployment
* Gitignore setup
	* Sqlite
* uWsgi, nginx setup
* Static files configure
* Setup logging
* Test domain ns

## Later
* Captcha (maybe)
* Change login position (maybe)
* Change star to smile (maybe)
* Add embed link/hyperlink option to copy direct link to review (maybe)
* Update search box to query more info (teacher name + school)
* Feedback feature
	* Simple one-way feedback form
	* Admin can get user's email, able to reply
	* https://github.com/girasquid/django-feedback
	* https://github.com/SpreadBand/django-backcap
* Empty star

## Require
* django-bleach
* bootstrap-rating (https://github.com/dreyescat/bootstrap-rating)
* jquery-scrollto
* bootbox
* python-social-auth
* readmore.js

## Completed
* Mobile design (Important!) (16-17)
	* ~~Teacher Info~~
	* ~~Review List~~
		* ~~Minor fix for edit/delete function~~
		* ~~Readmore~~
	* Navbar
		* ~~Fix search bar (Zooming problem, can copy google-style)~~
		* ~~Alignment problem~~
	* ~~Form page~~
		* ~~Use chrome devtools to check~~
		* ~~Reorder star rating up~~
	* ~~Multiple small fixes~~
		* ~~Add overall rating to desktop~~
		* ~~Image padding on mobile~~
		* ~~Smaller tags~~
* ~~Option for user to add/modify teacher's info (18-19)~~
	* ~~Link to image only, no direct upload~~
	* ~~To add:~~
		* ~~Option will be on menu bar or collapsed~~
	* ~~Use simple model, view in admin dashboard~~
* ~~Search box suggestion(vietnamese support if possible)~~
* ~~Social account linking and testing~~
* ~~User profile settings (only short_bio currently)~~
* ~~Adjust subject field for review form~~
	* ~~Change to simple TextField~~
	* ~~Autocomplete jquery with teacher's subject~~
* ~~Fake account option~~
* ~~Anonymous option~~
	* Think of some fun names to randomize
* ~~Two write review boxes~~
	* ~~Study~~
	* ~~Teacher~~
* ~~Optional voting (14-15)~~
	* ~~Dropdown, some values, optional~~
	* ~~Show majority percentage~~
	* ~~Select in form~~