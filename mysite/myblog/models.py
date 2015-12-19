from django.db import models
from django.contrib.auth.models import User
from django_bleach.models import BleachField
# User Model
class MyUser(models.Model):
	user = models.OneToOneField(User)
	profile_pic = models.ImageField(default='default-user-image.png')
	short_bio = models.CharField(max_length=100)
	name = models.CharField(max_length=100, default='Test User Display Name')
	
	def __unicode__(self):
		return self.user.username
		
# Tag Model
class Tag(models.Model):
	tag_name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.tag_name

# Entity Model
class Entity(models.Model):
	name = models.CharField(max_length=200)
	short_info = models.TextField()
	long_info = models.TextField()
	profile_pic = models.ImageField(default='default-user-image.png')
	is_teacher = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.name

# Review Model
class Review(models.Model):
	author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='author')
	entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='entity')
	date_written = models.DateField()
	#content = models.TextField()
	content = BleachField(allowed_tags=[
		'b'])
	title = models.CharField(max_length=200, default='NoTitle')
	

	rating_1 = models.IntegerField()
	rating_2 = models.IntegerField()
	rating_3 = models.IntegerField()
	rating_4 = models.IntegerField()
	rating_5 = models.IntegerField()

	tag_1 = models.ForeignKey(Tag, related_name='tag1')
	tag_2 = models.ForeignKey(Tag, related_name='tag2')
	tag_3 = models.ForeignKey(Tag, related_name='tag3')
	tag_4 = models.ForeignKey(Tag, related_name='tag4')
	tag_5 = models.ForeignKey(Tag, related_name='tag5')

	def __unicode__(self):
		return ' - by '.join([self.entity.name, self.author.user.username])

	class Meta:
		unique_together = ('author', 'entity')

# Vote Model
class Vote(models.Model):
	vote_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='vote_up_user')
	vote_review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='vote_down_review')
	vote_value = models.BooleanField()
	
	def __unicode__(self):
		return ' | '.join([self.vote_user.user.username, self.vote_review.__unicode__(), str(self.vote_value)])

	class Meta:
		unique_together = ('vote_user', 'vote_review')

# Criteria Name
class Criteria_Teacher(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Criteria_Uni(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name