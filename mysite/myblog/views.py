# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import MyUser, Tag, Entity, Review, Vote, Criteria_Teacher, Criteria_Uni, Subject
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
		review_tag_list = [each_review.tag_1, each_review.tag_2, each_review.tag_3, each_review.tag_4, each_review.tag_5]
		print review_tag_list
		review_tag_list = [item.id for item in review_tag_list if item]	
		print review_tag_list
		review_tag_list = [tag_list[item-1] for item in review_tag_list]
		print review_tag_list
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
	all_entity = get_all_entity_json()
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
	# add own vote details, add own_review if exists
	have_own_review = False
	own_review_id = None
	if request.user.is_authenticated():
		print "Logged in user", request.user.myuser.pk
		my_vote_list = Vote.objects.filter(vote_user__id=request.user.myuser.pk).values_list('vote_review_id', 'vote_value')
		print my_vote_list
		review_list = add_my_vote_info(review_list, my_vote_list)
		try:
			own_review = Review.objects.get(author_id=request.user.myuser.pk, entity_id=entity_id)
			print "Own Review exists"
			have_own_review = True
			own_review_id = own_review.id			
		except ObjectDoesNotExist:
			print "No existing review"			

	##########################
	return render(request, 'entity_guest.html', {
												'entity_info': entity_info,
												'review_list' : review_list,
												'entity_criteria' : entity_criteria,
												'entity_best_tag' : entity_best_tag,
												'have_own_review' : have_own_review,
												'own_review_id' : own_review_id,
												'all_entity' : all_entity,
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

def get_subject_list(entity_info):
	if entity_info.is_teacher:
		extra = ["Khác ()"]
		return json.dumps(list(entity_info.subjects.all().values_list('name', flat=True)) + extra)
	else:
		return None


def write_review(request, entity_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse(('show_entity'), args=(entity_id,)))

	all_entity = get_all_entity_json()
	if request.method == 'GET':
		entity_info = get_object_or_404(Entity, pk=entity_id)
		criteria_list = get_criteria_list(entity_info.is_teacher)
		tag_list = get_list_or_404(Tag)
		subject_list = get_subject_list(entity_info)
		print subject_list
		# check if the user already have a review?, edit mode
		# very ugly code, i know
		try:
			my_review = Review.objects.get(author_id=request.user.myuser.pk, entity_id=entity_id)
			print "Review already existed, proceed to fetch"
			selected_tag_list = []
			if my_review.tag_1:
				selected_tag_list.append(''.join(['tag', str(my_review.tag_1.id)]))
			if my_review.tag_2:
				selected_tag_list.append(''.join(['tag', str(my_review.tag_2.id)]))
			if my_review.tag_3:
				selected_tag_list.append(''.join(['tag', str(my_review.tag_3.id)]))
			if my_review.tag_4:
				selected_tag_list.append(''.join(['tag', str(my_review.tag_4.id)]))
			if my_review.tag_5:
				selected_tag_list.append(''.join(['tag', str(my_review.tag_5.id)]))
			return render(request, 'write_review.html', {
				'entity_info' : entity_info,
				'criteria_list' : criteria_list,
				'tag_list' : tag_list,
				'content' : my_review.content,
				'rating1': my_review.rating_1,
				'rating2': my_review.rating_2,
				'rating3': my_review.rating_3,
				'rating4': my_review.rating_4,
				'rating5': my_review.rating_5,
				'selected_tag_list' : selected_tag_list,
				'all_entity' : all_entity,
				'subject_list' : subject_list,
				'subject' : my_review.subject,
				'is_anonymous' : my_review.is_anonymous,
			})
		except ObjectDoesNotExist:
			return render(request, 'write_review.html', {
				'entity_info' : entity_info,
				'criteria_list' : criteria_list,
				'tag_list' : tag_list,
				'all_entity' : all_entity,
				'subject_list' : subject_list,
			})
	elif request.method == 'POST':
		# TODO: validate
		# populate data, currently ugly
		error = {}
		tag_id_list = Tag.objects.all().values_list('id', flat=True)
		selected_tag = [None, None, None, None, None]
		tag_count = 0
		for tag_id in tag_id_list:
			if request.POST.get(''.join(['tag',str(tag_id)])):
				if tag_count == 5:
					error["tag"] = True
					break
				selected_tag[tag_count] = tag_id
				tag_count += 1

		if tag_count < 3:
			error["tag"] = True
		if not request.POST.get('content'):
			error["content"] = True
		elif len(request.POST.get('content')) < 100:
			error["content"] = True
		if not (request.POST.get('rating1') and request.POST.get('rating2') \
				and request.POST.get('rating3') and request.POST.get('rating4') \
				and request.POST.get('rating5')):
			error["rating"] = True

		if error:
			entity_info = get_object_or_404(Entity, pk=entity_id)
			criteria_list = get_criteria_list(entity_info.is_teacher)
			tag_list = get_list_or_404(Tag)
			subject_list = get_subject_list(entity_info)
			form_selected_tag = []
			for tag_id in tag_id_list:
				if request.POST.get(''.join(['tag',str(tag_id)])):
					form_selected_tag.append(''.join(['tag',str(tag_id)]))

			print "Debug", request.POST.get('selected_subject')

			return render(request, 'write_review.html', {
				'entity_info' : entity_info,
				'criteria_list' : criteria_list,
				'tag_list' : tag_list,
				'subject_list' : subject_list,
				'error' : error,
				'content' : request.POST.get('content'),
				'rating1': request.POST.get('rating1', 0),
				'rating2': request.POST.get('rating2', 0),
				'rating3': request.POST.get('rating3', 0),
				'rating4': request.POST.get('rating4', 0),
				'rating5': request.POST.get('rating5', 0),
				'selected_tag_list' : form_selected_tag,
				'all_entity' : all_entity,
				'subject' : request.POST.get('subject'),
				'is_anonymous' : request.POST.get('is_anonymous'),
			})

		print "Checkbox value", request.POST.get('is_anonymous')
		try:
			print "No error validating review"
			print "Proceed to create or update review"
			Review.objects.update_or_create(
				author_id=request.user.myuser.pk,
				entity_id=entity_id,
				defaults={
					'content': request.POST.get('content'),
					'rating_1':request.POST.get('rating1'),
					'rating_2':request.POST.get('rating2'),
					'rating_3':request.POST.get('rating3'),
					'rating_4':request.POST.get('rating4'),
					'rating_5':request.POST.get('rating5'),
					'tag_1_id':selected_tag[0],
					'tag_2_id':selected_tag[1],
					'tag_3_id':selected_tag[2],
					'tag_4_id':selected_tag[3],
					'tag_5_id':selected_tag[4],
					'subject' : request.POST.get('subject'),
					'is_anonymous' : request.POST.get('is_anonymous', False),
				}
			)
			print "Review updated/created"
		except Exception, e:
			print traceback.print_exc()

		return HttpResponseRedirect(reverse(('show_entity'), args=(entity_id,)))

def delete_review(request, entity_id):
	try:
		if request.user.is_authenticated():
			try:
				review_to_delete = Review.objects.get(author_id=request.user.myuser.pk,entity_id=entity_id)
				print "Found review to delete"
				review_to_delete.delete()
				return HttpResponse("OK")
			except ObjectDoesNotExist:
				return None

		return None
	except Exception, e:
		print traceback.print_exc()

import json
from django.conf import settings

def get_all_entity_json():
	all_entity = Entity.objects.all().values('id', 'name', 'profile_pic', 'short_info')
	for entity in all_entity:
		entity["profile_pic"] = settings.MEDIA_URL + entity["profile_pic"]
		entity["url"] = reverse('show_entity', args=(entity["id"],))

	all_entity = [json.dumps(entity) for entity in all_entity]
	return all_entity


def show_index(request):
	all_entity = get_all_entity_json()
	return render(request, 'index.html', {
											'all_entity': all_entity,
		})

def write_profile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse(('show_entity'), args=(entity_id,)))

	all_entity = get_all_entity_json()
	if request.method == 'GET':
		# check if the user already have a profile, edit mode
		# very ugly code, i know
		short_bio = MyUser.objects.get(id=request.user.myuser.pk).short_bio
		return render(request, 'write_profile.html', {
				'all_entity' : all_entity,
				'short_bio' : short_bio,
				})
	elif request.method == 'POST':
		# TODO: validate
		# populate data, currently ugly
		try:
			user_obj = MyUser.objects.get(id=request.user.myuser.pk)
			user_obj.short_bio = request.POST.get('short_bio')
			user_obj.save()
			print "Profile updated"
		except Exception, e:
			print traceback.print_exc()

		return HttpResponseRedirect(reverse(('write_profile'), args=()))


# dev register
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class MyUserForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = ('profile_pic', 'short_bio', 'name')


def register(request):

	# A boolean value for telling the template whether the registration was successful.
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		myuser_form = MyUserForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and myuser_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			myuser = myuser_form.save(commit=False)
			myuser.user = user

			if 'profile_pic' in request.FILES:
				print 'Profile pic is transported'
				myuser.profile_pic = request.FILES['profile_pic']

			myuser.save()
			registered = True

		else:
			print user_form.errors, myuser_form.errors

	else:
		user_form = UserForm()
		myuser_form = MyUserForm()

	# Render the template depending on the context.
	return render(request,
			'registration/register.html',
			{'user_form': user_form, 'myuser_form': myuser_form, 'registered': registered} )