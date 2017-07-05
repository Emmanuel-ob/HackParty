#from newsfeed.models import Post, Like
from postApp.models import PollOption
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


# @register.filter
# def has_liked(post_id, user):
# 	attached_post = Post.objects.filter(pk = post_id)
# 	return Like.objects.filter(post = attached_post, liked_by = user).exists()

@register.filter
def poll_percent(post, response_opt):
	total_vote = post.get_vote_total()
	poll_opt   = PollOption.objects.filter(post=post, response=response_opt)[0]
	sub_vote  = poll_opt.vote
	if total_vote > 0:
		level = (sub_vote/total_vote) * 100
		return level
	return 0




# @register.filter
# def like_status(post, user):
# 	status = "",
# 	if Like.objects.filter(post = post, liked_by = user).exists():
# 		return 'Unlike'
# 	return 'Like'
	 