from django.conf.urls import url
from . import views


app_name = 'postApp'

urlpatterns = [

        url(r'^$', views.renderHome, name='index'), 
        url(r'^createPost$', views.get_post_page, name='get_post_page'), 
        url(r'^createPoll$', views.get_poll_page, name='get_poll_page'), 
        url(r'^health$', views.renderHealth, name='health'), 
        url(r'^fintech$', views.renderFintech, name='fintech'), 
        url(r'^agro$', views.renderAgro, name='agro'), 
        url(r'^education$', views.renderEducation, name='education'), 
        url(r'^ecommerce$', views.renderEcommerce, name='ecommerce'), 
        url(r'^virtual$', views.renderVirtual, name='virtual'), 
        url(r'^ai$', views.renderAI, name='artificial_i'), 
        url(r'^tag/$', views.createTag, name='tag'), 
        url(r'^edit/$', views.editPost, name='edit_post'), 
        url(r'^fullpost/(?P<post_id>\d+)$', views.postDetail, name='fullpost'), 
        url(r'^comment/(?P<post_id>\d+)$', views.commentPost, name='comment'), 
        url(r'^comment/delete/(?P<post_id>\d+)/(?P<comment_id>\d+)$', views.deleteComment, name='deleteComment'), 
        url(r'^comment/reply/(?P<post_id>\d+)/(?P<comment_id>\d+)$', views.replyComment, name='replyComment'), 
        url(r'^vote/(?P<post_id>\d+)/(?P<polloption_id>\d+)$', views.votePoll, name='vote'), 
        url(r'^delete/(?P<post_id>\d+)$', views.deletePost, name='deletePost'), 
        url(r'^create/$', views.createPostView, name = 'create_post'),
        url(r'^ajax/post/like/$', views.likePost, name = 'ajax_like_post'),
        url(r'^ajax/post/dislike/$', views.dislikePost, name = 'ajax_dislike_post'),
        url(r'^search/$', views.searchPost, name='search'),
        #url(r'^post/delete/(?P<post_id>[\w.@+-]+)/$', views.deletePostView, name = 'delete_post'),
        #url(r'^post/edit/(?P<post_id>[\w.@+-]+)/$', views.editPostView, name = 'edit_post'),
        #url(r'^ajax/post/like/$', views.likePostView, name = 'ajax_like_post'),
        #url(r'^post/share/(?P<post_id>[\w.@+-]+)/$', views.sharePostView, name = 'share_post'),
        #url(r'^post/comment/(?P<post_id>[\w.@+-]+)/$', views.allCommentPostView, name = 'comment_post'),
        #url(r'^post/comment/(?P<post_id>[\w.@+-]+)/send/$', views.commentPostView, name = 'make_comment'),
        #url(r'^post/view/(?P<post_id>[\w.@+-]+)/$', views.viewPostByTag, name = 'view_by_tag'),
        #url(r'^post/comment/$', views.commentPost, name = 'post_comment'),
        #url(r'^requests/fetch/$', views.fetchExternalSite, name = 'test_requests'),
        #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
 ]      