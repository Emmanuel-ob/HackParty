from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
    return "profile_images/%s_%s" % (str(time()).replace('.','_'), filename)


class UserPreference(models.Model):
	user           = models.ForeignKey(User, on_delete=models.CASCADE,)
	pref1          = models.CharField(max_length = 40)
	pref2          = models.CharField(max_length = 40)
	pref3          = models.CharField(max_length = 40)

	def __unicode__(self):
		return self.user.username 

	class Meta():
		verbose_name_plural  = 'UserPreference'

class UserProfile(models.Model):
	user           = models.OneToOneField(User, on_delete=models.CASCADE, related_name='joiner')
	gender         = models.CharField(max_length = 40, null=True)
	phoneNumber    = models.IntegerField(null=True, blank=True)
	confirm_key    = models.CharField(max_length = 50, default=None)
	is_active      = models.BooleanField(default=False)
	dob            = models.DateField(null=True, blank=True)
	stack          = models.CharField(max_length = 50, null=True,)
	git_url        = models.URLField(null=True, blank=True)
	description    = models.TextField(max_length = 1000, null=True,)
	image          = models.FileField(upload_to  = get_upload_file_name, null=True, blank=True)
	address        = models.CharField(max_length = 250, null=True,)
	state          = models.CharField(max_length = 40, null=True,)
	country        = models.CharField(max_length = 40, null=True,)
	
	
	def __unicode__(self):
		return self.user.username 

	class Meta():
		verbose_name_plural  = 'UserProfile'

