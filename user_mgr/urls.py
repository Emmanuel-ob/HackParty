from django.conf.urls import url
from . import views

app_name = 'user_mgr'
urlpatterns = [
    # url(r'^$', views.renderHome, name='index'),
    #url(r'^admin/$', views.renderAdmin, name = 'adminHome'),
    #url(r'^profile/$', views.getUserProfile, name = 'userProfile'),
    url(r'^signUp/$', views.get_signup_page, name = 'signUp'),
    # url(r'^signUp/(?P<nextpage>[\w.@+-]+)/$', views.get_signup_page, name = 'signUp'),
    url(r'^register/$', views.create_account, name = 'post_signUp'),
    url(r'^login/$', views.get_login_page, name ='login'),
    url(r'^signin/$', views.log_in, name ='signIn'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.get_profile, name='profile'),
    url(r'^resend/$', views.resend_link, name='resend_link'),
    url(r'^confirmation/(?P<token>[\w.@+-]+)/$', views.confirmAccount, name='confirmation'),
]