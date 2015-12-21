from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from models import MyUser, Tag, Entity, Review, Vote, Criteria_Teacher, Criteria_Uni
from collections import defaultdict
from django.core.exceptions import ObjectDoesNotExist
import traceback

def test_tag(request):
	tag_list = Tag.objects.all().values()
	return render(request, 'test_tag.html', {'tag_list' : tag_list})

def test_entity(request, entity_id):
	try:
		entity_id = int(entity_id)
	except ValueError:
		raise Http404()

	print "Fetching Info for Entity", entity_id
	entity_info = Entity.objects.get(id=entity_id)

	print entity_info
	return render(request, 'test_entity.html', {'entity_info' : entity_info})


def merge_dict(obj, new_dict):
	# merge django-orm class models with new dictionary
	for key, value in new_dict.items():
		setattr(obj, key, value)
	return obj

def calculate_overall(review_list, review_length):
	# Calculate the overall rating of an entity, supplied by review_list
	# Currently very ugly, will try to re-model later
	if review_length == 0:
		return [0.0, 0.0, 0.0, 0.0, 0.0]
	s = [0.0, 0.0, 0.0, 0.0, 0.0]
	for item in review_list:
		s[0] += item.rating_1
		s[1] += item.rating_2
		s[2] += item.rating_3
		s[3] += item.rating_4
		s[4] += item.rating_5
	
	s = [(item/review_length) for item in s]
	return s

def get_criteria_list(is_teacher):
	# return the list of criteria depending whether entity is teacher or uni
	if is_teacher:
		return get_list_or_404(Criteria_Teacher)
	else:
		return get_list_or_404(Criteria_Uni)

def add_vote_info(review_list):
	# add vote_up, vote_total, vote_percentage to each review
	for each_review in review_list:
		new_dict = {}
		up = Vote.objects.filter(vote_review__id=each_review.id, vote_value=True).count()
		down = Vote.objects.filter(vote_review__id=each_review.id, vote_value=False).count()
		if (up+down) == 0:
			percent = 0
		else:
			percent = int(100.0 * up / float(up+down))
		new_dict["vote_up"] = up
		new_dict["vote_total"] = up + down
		new_dict["vote_percent"] = percent
		each_review = merge_dict(each_review, new_dict)

	return review_list

def convert_rating_single(avg_score):
	# 3.5 -> (3,1) ; 3.0 -> (3,0); 3.9 -> (3,1)
	d = {}
	d["score_real"] = avg_score
	z = int(avg_score)
	d["score_full"] = z
	if (avg_score-z) > 0.0:
		d["score_half"] = 1
	else:
		d["score_half"] = 0
	return d


def faster_convert(each_score, criteria_name):
	d = convert_rating_single(each_score)
	d["name"] = criteria_name
	return d

def convert_rating_many(score_list, criteria_list):
	res = [faster_convert(each_score, criteria_list[idx]) for idx, each_score in enumerate(score_list)]
	return res

def add_rating_info(review_list, criteria_list):
	for each_review in review_list:
		score_list = [each_review.rating_1, each_review.rating_2, each_review.rating_3, each_review.rating_4, each_review.rating_5]
		rating_list = convert_rating_many(score_list, criteria_list)
		each_review.rating = rating_list
	return review_list

def add_tag_info(review_list, tag_list):
	tag_count = defaultdict(int)
	for each_review in review_list:
		review_tag_list = [each_review.tag_1.id, each_review.tag_2.id, each_review.tag_3.id, each_review.tag_4.id, each_review.tag_5.id]
		review_tag_list = [tag_list[item-1] for item in review_tag_list]
		each_review.tag_list = review_tag_list
		for item in review_tag_list:
			tag_count[item] += 1

	tag_list_with_count = tag_count.items()
	print tag_list_with_count
	tag_list_with_count = sorted(tag_list_with_count, key=lambda item: -item[1])	
	print tag_list_with_count
	return (review_list, tag_list_with_count[:5])

def add_my_vote_info(review_list, my_vote_list):
	if not my_vote_list:
		return review_list
	for each_review in review_list:
		for vote_info in my_vote_list:
			if vote_info[0] == each_review.id:
				each_review.have_own_vote = True
				each_review.own_vote = vote_info[1]
				break
	return review_list


def show_entity(request, entity_id):
	print "Fetch entity", entity_id

	entity_info = get_object_or_404(Entity, pk=entity_id)
	tag_list = get_list_or_404(Tag)
	print "Fetch tag"
	print tag_list

	#review_list = get_list_or_404(Review, entity__id=entity_id)
	review_list = Review.objects.filter(entity__id=entity_id)
	review_list = add_vote_info(review_list)
	print "Review List"
	print review_list
	
	entity_info.review_count = len(review_list)
	entity_score = calculate_overall(review_list, len(review_list))
	entity_avg_score = sum(entity_score) / len(entity_score)
	entity_info = merge_dict(entity_info, convert_rating_single(entity_avg_score))

	print 'Entity rating', entity_score
	print 'Entity Avg', entity_avg_score

	criteria_list = get_criteria_list(entity_info.is_teacher)
	print 'Criteria List', criteria_list

	entity_criteria = convert_rating_many(entity_score, criteria_list)
	review_list = add_rating_info(review_list, criteria_list)
	# TODO: sort review list

	(review_list, entity_best_tag) = add_tag_info(review_list, tag_list)
	print 'Best tag', entity_best_tag

	##### registered user section
	# add own vote details
	if request.user.is_authenticated():
		print "Logged in user", request.user.myuser.pk
		my_vote_list = Vote.objects.filter(vote_user__id=request.user.myuser.pk).values_list('vote_review_id', 'vote_value')
		print my_vote_list
		review_list = add_my_vote_info(review_list, my_vote_list)


	##########################
	return render(request, 'entity_guest.html', {
												'entity_info': entity_info,
												'review_list' : review_list,
												'entity_criteria' : entity_criteria,
												'entity_best_tag' : entity_best_tag,
												})
 

def change_vote(request, review_id, vote_value):
	# vote_value = 0(false), 1(true), 2(cancel)
	# check user logged in, user own this vote
	valid_vote = [0, 1, 2]
	try:
		vote_value = int(vote_value)
		review_id = int(review_id)
		print request.path, request.user.id, request.user.myuser.id
		print "Receive ajax", review_id, vote_value
		if request.user.is_authenticated():
			if vote_value == 2:
				print "Delete vote"
				target_vote = get_object_or_404(Vote, vote_user_id=request.user.myuser.id, vote_review_id=review_id)
				target_vote.delete()
			else:
				try:
					target_vote = Vote.objects.get(vote_user__id=request.user.myuser.id, vote_review__id=review_id)
					target_vote.vote_value = vote_value
					target_vote.save()
					print "Update vote"
				except ObjectDoesNotExist:
					print "Create vote"
					target_vote = Vote.objects.create(vote_user_id=request.user.myuser.id, vote_review_id=review_id, vote_value=vote_value)
	except Exception, e:
		return HttpResponse("Error AJAX", request.path)		
	return HttpResponse("OK")


	