from django import forms
from django.contrib.auth.models import User
from postApp.models import Post, Comment


class PostForm(forms.ModelForm):
    title               =   forms.CharField(max_length = 100, help_text = '', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'title', 'required': 'required'}))
    body                =   forms.CharField(max_length= 2000, help_text="", widget=forms.Textarea(attrs= {'class' : 'form-control', 'placeholder' : 'Content', 'required' : 'required'}))
    #tag                 =   forms.CharField(max_length= 25, help_text="", widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Tag', 'required' : 'required'}))
    #image               =   forms.FileField(widget=forms.FileInput())
    
    class Meta:
        model = Post
        fields = ( 'title',  'body', )

class CommentForm(forms.ModelForm):
    body       = forms.CharField(max_length = 2000, help_text = 'characters.', widget = forms.Textarea(attrs = {'class': 'form-control', 'rows': '2', 'cols': '80', 'placeholder': 'Your comment', 'required': 'required'}))
   
    class Meta:
        model = Comment
        fields = ('body',)

