from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
    return "profile_images/%s_%s" % (str(time()).replace('.','_'), filename)


class PostManager(models.Manager):

	def get_visible_posts(self):
		return self.get_queryset().filter(is_hidden = False)

	def get_hidden_posts(self):
		return self.get_queryset().filter(is_hidden = True)

	def get_user_posts(self, user):
		return self.get_queryset().filter(posted_by = user, is_hidden = False).order_by('-date_posted')


class Tag(models.Model):
	tag_name  = models.CharField(max_length = 100)


class Post(models.Model):
	posted_by     = models.ForeignKey(User)
	date_posted   = models.DateTimeField(auto_now_add = True)
	date_updated  = models.DateTimeField(auto_now = True)
	title         = models.CharField(max_length = 100)
	body          = models.TextField(max_length = 3000)
	tag           = models.ForeignKey('Tag', default=None)
	post_type     = models.CharField(max_length = 40) #either post or poll
	is_hidden     = models.BooleanField(default= False)
	image         = models.FileField(upload_to  = get_upload_file_name, null=True, blank=True)
	objects       = PostManager()

	def __unicode__(self):
		return '%s'  %(self.posted_by.username)

	def get_comments(self):
		return self.comment_set.all().order_by('-date_commented')

	def get_vote_total(self):
		options  = self.polloption_set.all()
		total = 0
		for option in options:
			total += option.vote
		return total

	def get_percent(self, response):
		total = self.get_vote_total()
		if total ==0:
			return 0
		else:
			option = self.polloption_set.filter(response=response)[0]
			sub_total = option.vote
			percent = (sub_total/total) * 100
			return percent
			

	class Meta:
		ordering =['-date_posted', '-date_updated']



class Like(models.Model):
	post        = models.ForeignKey('Post', null = True)
	liked_by    = models.ForeignKey(User, null=True)
	date_liked  = models.DateTimeField(auto_now_add= True, null=True)
	comment     = models.ForeignKey('Comment', null=True)

	def __unicode__(self):
		return self.liked_by.username

class DisLike(models.Model):
	post        = models.ForeignKey('Post', null = True)
	disliked_by = models.ForeignKey(User, null=True)
	date_liked  = models.DateTimeField(auto_now_add= True, null=True)
	comment     = models.ForeignKey('Comment', null=True)

	def __unicode__(self):
		return self.liked_by.username


class Comment(models.Model):
	post           = models.ForeignKey('Post', null = True)
	comment_by     = models.ForeignKey(User)
	body           = models.TextField(max_length = 1000)
	date_commented = models.DateTimeField(auto_now_add= True, null=True)
	date_updated   = models.DateTimeField(auto_now= True, null=True)
	is_hidden      = models.BooleanField(default= False)

	def __unicode__(self):
		return self.comment_by.username 

	def get_replies(self):
		return self.reply_set.all().order_by('-date_replied')

	class Meta:
		ordering =['-date_commented', '-date_updated']

class Reply(models.Model):
	comment        = models.ForeignKey('Comment', on_delete=models.CASCADE,)
	body           = models.TextField(max_length = 1000)
	reply_by       = models.ForeignKey(User)
	date_replied   = models.DateTimeField(auto_now_add= True)
	date_updated   = models.DateTimeField(auto_now= True)

	def __unicode__(self):
		return self.comment.post.title

	class Meta:
		ordering =['-date_replied',]

class PollOption(models.Model):
	response      = models.CharField(max_length = 100, )
	post          = models.ForeignKey('Post', on_delete=models.CASCADE, )
	colour        = models.CharField(max_length=20, default='green')
	vote          = models.IntegerField(default=0)

	def __unicode__(self):
		return self.poll.title

	def get_vote_count(self):
		return self.vote


# class Vote(models.Model):
# 	response       = models.ForeignKey('PollOption', null=True)
# 	poll           = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
# 	vote_by        = models.ForeignKey(User, null=True)

# 	def __unicode__(self):
# 		return self.response