from django.contrib import admin

# Register your models here.
from newsfeed.models import Like, Comment, Post, DisLike, Reply

class PostAdmin(admin.ModelAdmin):
	list_display = ['posted_by', 'date_posted', 'is_hidden']
	list_filter  = ['is_hidden']

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(DisLike)
admin.site.register(Reply)

