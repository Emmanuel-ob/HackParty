from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
	title          = models.CharField(max_length = 100)
	content        = models.TextField(max_length = 3000)
	tag_id         = models.IntegerField()
	created_by     = models.ForeignKey(User)
	date_posted    = models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		return self.created_by.username


class PollOptions(models.Model):
	response      = models.CharField(max_length = 100)
	poll          = models.ForeignKey(Poll, on_delete=models.CASCADE,)

	def __unicode__(self):
		return self.poll.title

# class Vote(models.Model):
# 	response_id    = models.IntegerField()
# 	poll           = models.ForeignKey(Poll, on_delete=models.CASCADE,)
# 	vote_by        = models.ForeignKey(User)

# 	def __unicode__(self):
# 		return self.response_id

