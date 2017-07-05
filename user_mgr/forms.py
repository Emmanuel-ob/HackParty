from django import forms
from django.contrib.auth.models import User
from user_mgr.models import UserProfile

# CHOICES = (('male', 'male',), ('female', 'female',))
# choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class RegistrationForm(forms.ModelForm):
    username   = forms.CharField(max_length = 120, help_text = 'characters.', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Username', 'required': 'required'}))
    first_name = forms.CharField(max_length = 120, help_text = '', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}))
    last_name  = forms.CharField(max_length = 120, help_text = '',  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Surname', 'required': 'required'}))
    email      = forms.EmailField(max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'email@example.com', 'required': 'required'}))
    password   = forms.CharField(max_length = 20, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'password', 'required': 'required'}))
   
    class Meta:
        model  = User
        fields = ('username','first_name', 'last_name', 'email', 'password',)

class LoginForm(forms.ModelForm):
    email    = forms.EmailField(max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'email@example.com', 'required': 'required'}))
    password = forms.CharField(max_length = 15, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'password', 'required': 'required'}))
    
    class Meta:
        model  = User
        fields = ('email', 'password',)

class UserProfileForm(forms.ModelForm):
    # gender              =   forms.CharField(max_length= 25, help_text="", widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Gender', 'required' : 'required'}))
    phone_number        =   forms.CharField(max_length = 20, help_text = '', widget = forms.NumberInput(attrs = {'class': 'form-control', 'placeholder': 'PhoneNumber', 'required': 'required'}))
    date_of_birth       =   forms.DateField(help_text="", widget=forms.DateInput(attrs= {'class' : 'form-control', 'placeholder' : '1990-03-23', 'required' : 'required'}))
    address             =   forms.CharField(max_length= 250, help_text="", widget=forms.Textarea(attrs= {'class' : 'form-control', 'rows': '2', 'cols': '80', 'placeholder' : 'Address', 'required' : 'required'}))
    state               =   forms.CharField(max_length= 25, help_text="", widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'State', 'required' : 'required'}))
    country             =   forms.CharField(max_length= 25, help_text="", widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'description', 'required' : 'required'}))
    description         =   forms.CharField(max_length= 300, help_text="", widget=forms.Textarea(attrs= {'class' : 'form-control', 'rows': '2', 'cols': '80', 'placeholder' : 'describe Yourself', 'required' : 'required'}))
    # display_status      =   forms.CharField(max_length= 150, help_text="", widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Country', 'required' : 'required'}))
    #image               =   forms.FileField(widget=forms.FileInput())
    git_url             =   forms.URLField(max_length = 100, initial='http://', help_text = '',  widget = forms.URLInput(attrs = {'class': 'form-control', 'placeholder': 'password', 'required': 'required'}))
    stack               =   forms.CharField(max_length = 120, help_text = '',  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'e.g Fronend, Backend, Fullstack', 'required': 'required'}))
    
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'date_of_birth', 'address', 'state', 'country', 'description', 'git_url', 'stack',)



