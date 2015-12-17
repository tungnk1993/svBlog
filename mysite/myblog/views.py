from django.shortcuts import render
from django.http import HttpResponse, Http404
from models import MyUser, Tag, Entity, Review, Vote, Criteria_Teacher, Criteria_Uni

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


def test_review(request):
	'''
	- Get entity_info as normal
	- Grab review
	- Calculate rating
	- Calculate tag
	- Each review, count upvote downvote
	'''
	pass

def show_entity(request, entity_id):
	print "Fetch entity", entity_id

	return render(request, 'entity_guest.html')
	'''
	return render(request, 'entity_guest.html', {
													'entity_info': entity_info,
													'entity_best_tag' : entity_best_tag,
													'entity_criteria' : entity_criteria,
													'review_list' : review_list,
												})
	'''


	