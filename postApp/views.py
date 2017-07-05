from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
#from user_mgr.models import UserProfile, UserPreference
from postApp.models import Post, Comment, Like, DisLike, Tag, PollOption, Reply
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from postApp.forms import PostForm, CommentForm

from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
#from django.contrib.sites.models import Site
#import requests as req
#
#domain = Site.objects.get_current().domain
#from django.contrib.sites.shortcuts import get_current_site




def createTag(request):
	if request.method == 'POST':
		rp = request.POST
		new_tag = Tag.objects.create(tag_name=rp['tag_name'])
		new_tag.save()
		if new_tag:
			messages.success(request, 'Tag was created!')
			return render(request, 'postApp/tag.html')
	return render(request, 'postApp/tag.html')

def renderHome(request):
    context = {
        'posts': Post.objects.filter(is_hidden=False),
        'post_form': PostForm()
    }
    return render(request, 'postApp/forum.html', context)

@login_required()
def get_post_page(request):
    context = {
        'post_form': PostForm()
        }
    return render(request, 'postApp/post.html', context)

@login_required()
def get_poll_page(request):
    context = {
        'post_form': PostForm()
        }
    return render(request, 'postApp/poll.html', context)

def renderHealth(request):
    tag = Tag.objects.filter(tag_name='health')
    context = {
        'posts': Post.objects.filter(is_hidden=False, tag=tag),
        'post_form': PostForm()
    }
    return render(request, 'postApp/health.html', context)

def renderFintech(request):
    tag = Tag.objects.filter(tag_name='fintech')
    context = {
        'posts': Post.objects.filter(is_hidden=False, tag=tag),
        'post_form': PostForm()
    }
    return render(request, 'postApp/fintech.html', context)

def renderAgro(request):
    tag = Tag.objects.filter(tag_name='agro')
    context = {
        'posts': Post.objects.filter(is_hidden=False, tag=tag),
        'post_form': PostForm()
    }
    return render(request, 'postApp/agro.html', context)

def renderEducation(request):
    tag = Tag.objects.filter(tag_name='education')
    context = {
        'posts': Post.objects.filter(is_hidden=False, tag=tag),
        'post_form': PostForm()
    }
    return render(request, 'postApp/education.html', context)

def renderEcommerce(request):
    tag = Tag.objects.filter(tag_name='ecommerce')
    context = {
        'posts': Post.objects.filter(is_hidden=False, tag=tag),
        'post_form': PostForm()
    }
    return render(request, 'postApp/ecommerce.html', context)

def renderVirtual(request):
    tag = Tag.objects.filter(tag_name='virtual')
    context = {
        'posts': Post.objects.filter(is_hidden=False, tag=tag),
        'post_form': PostForm()
    }
    return render(request, 'postApp/virtual.html', context)

def renderAI(request):
    tag = Tag.objects.filter(tag_name='ai')
    context = {
        'posts': Post.objects.filter(is_hidden=False, tag=tag),
        'post_form': PostForm()
    }
    return render(request, 'postApp/artificial.html', context)



@login_required()
def createPostView(request):
	if request.method == "POST":
		rp = request.POST
		rf = request.FILES
		post_form = PostForm(request.POST)
		
		if post_form.is_valid():
			title    = post_form.cleaned_data.get('title')
			print title + '\n\n'
			body     = post_form.cleaned_data.get('body')
			post_tag      = Tag.objects.get(tag_name = rp['tag'])
			 
			if rp['post_type'] == 'post':
				new_post = Post.objects.create(posted_by = request.user, title=title, body = body, tag=post_tag, post_type= rp['post_type'],)
				print request.user
				if len(request.FILES) != 0:
				#if request.FILES['image']:
					new_post.image = rf['image']
				new_post.save()
				if new_post:
					messages.success(request, "Post have been saved.")
					return redirect(reverse("postApp:index"))
				else:
					messages.debug(request, "Sorry your post was not saved at this time, pls try again")
					return redirect(reverse("postApp:index"))
			else:
				new_post = Post.objects.create(posted_by = request.user, title=title, body = body, tag=post_tag, post_type= rp['post_type'],)
				if len(request.FILES) != 0:
				#if request.FILES['image']:
					new_post.image = rf['image']
				new_post.save()
				response_1 = PollOption.objects.create(response=rp['response_1'], post=new_post, colour='green')
				response_1.save()
				response_2 = PollOption.objects.create(response=rp['response_2'], post=new_post, colour='blue')
				response_2.save()
				if rp['response_3'] !='':
					response_3 = PollOption.objects.create(response=rp['response_3'], post=new_post, colour='red')
					response_3.save()
				if new_post:
					messages.success(request, "Post have been saved.")
					return redirect(reverse("postApp:index"))
				else:
					messages.debug(request, "Sorry your post was not saved at this time, pls try again")
					return redirect(reverse("postApp:index"))
		else:
			messages.warning(request, "Invalid inputs")
			return redirect(reverse("postApp:index"))
		
	else:
		messages.warning(request, "Invalid request!")
		return redirect(reverse("postApp:index"))
        
@login_required()
def editPost(request):
	if request.method == "POST":
		rp = request.POST
		rf = request.FILES
		if rp['post_type'] == 'post':
			edit_post       = Post.objects.get(id=rp['post_id'])
			edit_post.title = rp['title']
			edit_post.body  = rp['body']
			if rp['tag'] !='':
				post_tag        = Tag.objects.get(tag_name = rp['tag'])
				edit_post.tag   = post_tag
			if len(request.FILES) != 0:
				if edit_post.image !='':
					edit_post.image.delete()
				edit_post.image = rf['image']
			edit_post.save()
			if edit_post:
				messages.success(request, "Post have been modified successfully.")
				return redirect(reverse("postApp:index"))
			else:
				messages.debug(request, "Sorry your post was not modified at this time, pls try again")
				return redirect(reverse("postApp:index"))
		else:
			messages.warning(request, "Invalid request channel!")
			return redirect(reverse("postApp:index"))
		
	else:
		messages.warning(request, "Invalid request!")
		return redirect(reverse("postApp:index"))


def postDetail(request, post_id):
	context = {}
	if Post.objects.filter(id=post_id).exists():
		the_post = Post.objects.get(id=post_id)
		context  = {'post':the_post,
		             'comment_form': CommentForm(),
		            }
	return render(request, 'postApp/postDetail.html', context)

@login_required()
def commentPost(request, post_id):
	context = {}
	if request.method == "POST":
		rp = request.POST
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			body    = comment_form.cleaned_data.get('body')
			if Post.objects.filter(id=post_id).exists():
				the_post    = Post.objects.get(id=post_id)
				new_comment = Comment.objects.create(post=the_post, comment_by=request.user, body=body)
				if new_comment:
					messages.success(request, 'Your reaction have been recorded!')
				else:
					messages.debug(request, 'Your reaction was not recorded, try again!')
			else:
				messages.warning(request, 'The post no longer exist')
		else:
			messages.warning(request, 'Invalid inputs')
	else:
		messages.warning(request, 'Invalid request')
	return redirect(reverse("postApp:fullpost", kwargs = {'post_id':post_id}))


@login_required()
def deleteComment(request, post_id, comment_id):
	if Post.objects.filter(id=post_id).exists():
		if Comment.objects.filter(id=comment_id).exists():
			delete_comment = Comment.objects.get(id=comment_id)
			delete_comment.delete()
			if delete_comment:
				messages.success(request, 'Your comment have been removed!')
			else:
				messages.debug(request, 'Your comment was not removed, try again!')
		else:
			messages.warning(request, 'The comment no longer exist')
		#return render(request, 'postApp/postDetail.html', context)
		return redirect(reverse("postApp:fullpost", kwargs = {'post_id':post_id}))
	else:
		return render(request, 'user_mgr/404.html')

@login_required()
def replyComment(request, post_id, comment_id):
	if Post.objects.filter(id=post_id).exists():
		if request.method == "POST":
			rp = request.POST
			if Comment.objects.filter(id=comment_id).exists():
				comment = Comment.objects.get(id=comment_id)
				reply  = Reply.objects.create(comment=comment, body=rp['body'], reply_by=request.user)
				if reply:
					messages.success(request, 'Your reply have been recorded!')
				else:
					messages.debug(request, 'Your reply was not recorded, try again!')
			else:
				messages.warning(request, 'The comment no longer exist')
			return redirect(reverse("postApp:fullpost", kwargs = {'post_id':post_id}))
		else:
			return render(request, 'user_mgr/404.html')
	else:
		return render(request, 'user_mgr/404.html')


@login_required()
def deletePost(request, post_id):
	if Post.objects.filter(id=post_id).exists():
		the_post    = Post.objects.get(id=post_id)
		the_post.delete()
		if the_post:
			messages.success(request, 'The select post have been removed!')
		else:
			messages.debug(request, 'Your selected post was not removed, try again!')
	else:
		messages.warning(request, 'The post no longer exist')
	return redirect(reverse("postApp:index"))

@login_required()
def likePost(request, post_id=None):
	# check if user has like the post previously
	post_attached = Post.objects.filter(pk = request.GET.get('post_Id', ""))
	if post_attached.count() > 0:
		if not DisLike.objects.filter(disliked_by = request.user, post = post_attached[0]).exists():
			if not Like.objects.filter(liked_by = request.user, post = post_attached[0]).exists():
				Like.objects.create(post = post_attached[0], liked_by = request.user)
			else:
				Like.objects.filter(post = post_attached[0], liked_by = request.user).delete()
		else:
			DisLike.objects.filter(post = post_attached[0], disliked_by = request.user).delete()
			Like.objects.create(liked_by = request.user, post = post_attached[0])
	else:
		messages.info(request, "sorry this post no longer exists.")
	return JsonResponse({'post_like_count':post_attached[0].like_set.count(),
		                  'post_dislike_count':post_attached[0].dislike_set.count()})

@login_required()
def dislikePost(request, post_id=None):
	# check if user has like the post previously
	post_attached = Post.objects.filter(pk = request.GET.get('post_Id', ""))
	#post_attached = Post.objects.filter(pk = post_id)
	if post_attached.count() > 0:
		if not Like.objects.filter(liked_by = request.user, post = post_attached[0]).exists():
			if not DisLike.objects.filter(disliked_by = request.user, post = post_attached[0]).exists():
				DisLike.objects.create(post = post_attached[0], disliked_by = request.user)
			else:
				DisLike.objects.filter(post = post_attached[0], disliked_by = request.user).delete()
		else:
			Like.objects.filter(post = post_attached[0], liked_by = request.user).delete()
			DisLike.objects.create(disliked_by = request.user, post = post_attached[0])
	else:
		messages.info(request, "sorry this post no longer exists.")
	return JsonResponse({'post_dislike_count':post_attached[0].dislike_set.count(),
		                  'post_like_count':post_attached[0].like_set.count()})

def searchPost(request):
    if request.method =="POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    posts = Post.objects.filter(title__icontains=search_text)[0:15]
    return render(request, 'postApp/ajax_search.html', {'posts': posts})

def votePoll(request, post_id, polloption_id):
	post_involved = Post.objects.filter(id=post_id)[0]
	user = None
	if post_involved:
		response = PollOption.objects.filter(id=polloption_id, post=post_involved)[0]
		if response:
			response.vote += 1
			response
			response.save()
			print response.vote
			messages.success(request, 'Your vote have been recorded')
		else:
			messages.warning(request, 'Poll option does not exist')
	else:
		messages.error(request, 'Poll no longer open')
	return redirect(reverse("postApp:index"))



