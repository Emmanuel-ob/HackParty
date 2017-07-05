from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from user_mgr.models import UserProfile, UserPreference
from postApp.models import Post
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
from user_mgr.forms import RegistrationForm, LoginForm, UserProfileForm
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.core import mail
from django.conf import settings
from django.utils.crypto import get_random_string 
from django.template.loader import render_to_string
#from django.views.generic import RedirectView
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader, Context, RequestContext
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site



def get_signup_page(request):
    context = {
    'reg_form': RegistrationForm()
    }
    return render(request, 'user_mgr/signup.html', context)



def get_login_page(request):
    context = {
    'login_form': LoginForm()
    }
    return render(request, 'user_mgr/login.html', context)

@login_required()
def get_profile(request, username):
    profile_form =  UserProfileForm()
    context  ={'profile_form': profile_form,
                'profile': UserProfile.objects.filter(user=request.user)[0] }
    if request.method == 'POST':
        user_profile_form = UserProfileForm(data=request.POST)
        rp = request.POST
        if user_profile_form.is_valid():
            phoneNumber = user_profile_form.cleaned_data.get('phone_number')
            dob         = user_profile_form.cleaned_data.get('date_of_birth')
            address     = user_profile_form.cleaned_data.get('address')
            state       = user_profile_form.cleaned_data.get('state')
            country     = user_profile_form.cleaned_data.get('country')
            description = user_profile_form.cleaned_data.get('description')
            git_url     = user_profile_form.cleaned_data.get('git_url')
            stack       = user_profile_form.cleaned_data.get('stack')
            gender      = rp['gender']
            # image       = request.FILES['image']
            
            user = User.objects.filter(email=request.user.email)[0]
            if user:
                user_profile             = UserProfile.objects.get(user=user)
                user_profile.phoneNumber = phoneNumber
                user_profile.dob         = dob
                user_profile.stack       = stack
                user_profile.gender      = gender
                user_profile.git_url     = git_url
                user_profile.description = description
                user_profile.address     = address
                user_profile.state       = state
                user_profile.country     = country
                if len(request.FILES)    != 0:
                    if user_profile.image !='':
                        user_profile.image.delete()
                    user_profile.image    =request.FILES['image']
                user_profile.save()
                if user_profile:
                     messages.success(request, 'Your profile have been saved')
                else:
                     messages.debug(request, 'Something went wrong, please try again')
        else:
            context  ={'profile_form': UserProfileForm(data = request.POST),
                'profile': UserProfile.objects.filter(user=request.user)[0] }
            messages.warning(request, 'Invalid inputs!! please check & try again!')
    return render(request, 'user_mgr/profile.html', context)
    
def confirmAccount(request, token):
    check_user = UserProfile.objects.filter(confirm_key = token, is_active = False)
    if check_user.exists():
        check_user = check_user[0]
        #check_user.update(is_active=True, confirm_key='',)
        check_user.is_active = True
        check_user.confirm_key = ""
        check_user.save()
        email =   check_user.user.email
        username = check_user.user.username
        username = User.objects.get(email=email, username=username)
        username.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, username)
        messages.success(request, 'Your account have been confirmed')
        return redirect(reverse('postApp:index'))
    else:
        return render(request, 'user_mgr/unconfirmed.html')

def resend_link(request):
    if request.method == 'POST':
        rp = request.POST
        if User.objects.filter(email= rp['email']).exists():
            user          = User.objects.get(email=rp['email'])
            username      = user.username
            unique_token  = get_random_string(length=32)
            if  UserProfile.objects.filter(user=user).exists():
                profile       = UserProfile.objects.get(user=user)
                if not profile.confirm_key == null:
                    profile.confirm_key.delete()
                    profile.confirm_key = unique_token
                    profile_saved = profile.save()
                    if profile_saved:
                        # update_url   = "http://10.100.200.156:8000/user/confirmation/" + unique_token
                        # subject      = 'HackPart Account Confirmation'
                        # message      = "Thank you for signing up on the hackparty platform. Please click on the link to confirm your account: " + update_url
                        # from_email   = settings.EMAIL_HOST_USER
                        # to_email     = [rp['email'], from_email]
                        # send_mail(subject, message, from_email, to_email, fail_silently=True,)
                        try:
                            subject      = 'HackParty Account Confirmation'
                            from_email   = settings.EMAIL_HOST_USER
                            to_email     = [email, from_email]
                            text_content = "Thank you for signing up on the hackparty platform. Please click on the link below to confirm your account: \n\n"
                            domain = get_current_site(request).domain
                            #print domain
                            html_content = text_content + "http://" + domain + "/user/confirmation/" + unique_token
                            msg = EmailMultiAlternatives(subject, text_content, from_email, to_email,)
                            msg.attach_alternative(html_content, "text/html")
                            msg.send()
                            messages.success(request, 'Your account details have been saved')
                            return render(request, 'user_mgr/success.html', {'username': username})
                        except:
                              return render(request, 'user_mgr/unsuccess.html', {'username': username})
                else:
                    profile.confirm_key = unique_token
                    profile_saved       = profile.save()
                    if profile_saved:
                        
                        try:
                            subject      = 'HackParty Account Confirmation'
                            from_email   = settings.EMAIL_HOST_USER
                            to_email     = [email, from_email]
                            text_content = "Thank you for signing up on the hackparty platform. Please click on the link below to confirm your account: \n\n"
                            domain = get_current_site(request).domain
                            #print domain
                            html_content = text_content + "http://" + domain + "/user/confirmation/" + unique_token
                            msg = EmailMultiAlternatives(subject, text_content, from_email, to_email,)
                            msg.attach_alternative(html_content, "text/html")
                            msg.send()
                            messages.success(request, 'Your account details have been saved')
                            return render(request, 'user_mgr/success.html', {'username': username})
                        except:
                              return render(request, 'user_mgr/unsuccess.html', {'username': username})
                    return render(request, 'user_mgr/unsuccess.html', {'username': username})
            else:
                profile       = UserProfile.objects.create(user=user, confirm_key=unique_token)
                profile_saved = profile.save()
                if profile_saved:
                    
                    try:
                        subject      = 'HackParty Account Confirmation'
                        from_email   = settings.EMAIL_HOST_USER
                        to_email     = [email, from_email]
                        text_content = "Thank you for signing up on the hackparty platform. Please click on the link below to confirm your account: \n\n"
                        domain = get_current_site(request).domain
                        #print domain
                        html_content = text_content + "http://" + domain + "/user/confirmation/" + unique_token
                        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email,)
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                        messages.success(request, 'Your account details have been saved')
                        return render(request, 'user_mgr/success.html', {'username': username})
                    except:
                          return render(request, 'user_mgr/unsuccess.html', {'username': username})
                return render(request, 'user_mgr/unsuccess.html', {'username': username})
        messages.warning(request, 'You have not signed up with this email before. Click on signup to signup!')
        return render(request, 'user_mgr/unconfirmed.html')

    messages.warning(request, 'Invalid request!')
    return render(request, 'user_mgr/unconfirmed.html')




def create_account(request):
    reg_form =  RegistrationForm()
    context  ={'reg_form': reg_form}
    if request.method == 'POST':
        user_reg_form = RegistrationForm(data=request.POST)

        rp = request.POST
        
        if User.objects.filter(email = rp['email']).exists():
            #context['reg_form'] = RegistrationForm(data = request.POST)
            messages.info(request, 'Sorry this email has been taken')
            return redirect(reverse('user_mgr:signUp'))
        else:
            if user_reg_form.is_valid():
            	#print rp['email'] + '\n\n'
            	username   = user_reg_form.cleaned_data.get('username')
            	email      = user_reg_form.cleaned_data.get('email')
            	first_name = user_reg_form.cleaned_data.get('first_name')
            	last_name  = user_reg_form.cleaned_data.get('last_name')
            	password   = user_reg_form.cleaned_data.get('password')
                user       = User.objects.create(username = username, first_name = first_name, last_name = last_name, email = email,)
                user.set_password(password)
                user.save()
                if user:
                    unique_token  = get_random_string(length=32)
                    profile       = UserProfile.objects.create(user=user, confirm_key=unique_token)
                    profile_saved = profile.save()
                    #print settings.EMAIL_HOST_USER
                    if profile:
                        try:
                            subject      = 'HackParty Account Confirmation'
                            from_email   = settings.EMAIL_HOST_USER
                            to_email     = [email, from_email]
                            text_content = "Thank you for signing up on the hackparty platform. Please click on the link below to confirm your account: \n\n"
                            domain = get_current_site(request).domain
                            #print domain
                            html_content = text_content + "http://" + domain + "/user/confirmation/" + unique_token
                            msg = EmailMultiAlternatives(subject, text_content, from_email, to_email,)
                            msg.attach_alternative(html_content, "text/html")
                            msg.send()
                            messages.success(request, 'Your account details have been saved')
                            return render(request, 'user_mgr/success.html', {'username': username})
                        except:
                            messages.debug(request, 'Your account details may not have been saved correctly')
                            return render(request, 'user_mgr/unsuccessful.html', {'username': username})
                else:
                    messages.warning(request, 'something went wrong acount not created!! please try again!')
            else: 
                messages.warning(request, 'something went wrong acount not created!! please try again!')
                return render(request, 'user_mgr/signup.html')
    return redirect(reverse( 'user_mgr:signUp'))





def log_in(request):
    if request.method == 'POST':
        rp = request.POST
        login_form = LoginForm(data = request.POST)
        if User.objects.filter(email = rp['email']).exists():
            user    = User.objects.get(email= rp['email'])
            username = user.username
            status = UserProfile.objects.get(user = user).is_active
            auth_user = authenticate(username= username, password = rp['password'])
            if auth_user:
                login(request, auth_user)
                if status == True:
                    if not rp['next'] == '':
                        print rp['next']
                        messages.success(request, 'You are logged in!')
                        return redirect(rp['next'])
                    else: 
                        messages.success(request, 'You are logged in!')
                        return redirect(reverse('postApp:index'))
                else:
                    messages.error(request, 'Your account is inactive! Check your email for activation link or contact admin!!')
                    return redirect(reverse('user_mgr:login'))
            else: 
                messages.error(request, 'Sorry your email or password is incorrect!!')
        else:
            messages.error(request, 'Sorry this email adddress doest not exist!!')
    return redirect(reverse('user_mgr:login'))
    

def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect(reverse('postApp:index'))



# def send_templated_email(subject, email_template_name, email_context, recipients, sender=None, bcc=None, fail_silently=True, files=None):
#     c = Context(email_context)
#     if not sender:
#         sender = settings.DEFAULT_FROM_EMAIL

#     template = loader.get_template(email_template_name)
    
#     text_part = strip_tags(template.render(c))
#     html_part = template.render(c)
    
#     if type(recipients) == str:
#         if recipients.find(','):
#             recipients = recipients.split(',')
#     elif type(recipients) != list:
#         recipients = [recipients,]
        
#     msg = EmailMultiAlternatives(subject,
#                                 text_part,
#                                 sender,
#                                 recipients,
#                                 bcc=bcc)
#     msg.attach_alternative(html_part, "text/html")

#     if files:
#         if type(files) != list:
#             files = [files,]

#         for file in files:
#             msg.attach_file(file)

#     return msg.send(fail_silently)







# def create_account(request):
#     reg_form =  RegistrationForm()
#     context  ={'reg_form': reg_form}
#     if request.method == 'POST':
#         #user = None
#         user_reg_form = RegistrationForm(data=request.POST)

#         rp = request.POST
        
#         if User.objects.filter(email = rp['email']).exists():
#             #context['reg_form'] = RegistrationForm(data = request.POST)
#             messages.info(request, 'Sorry this email has been taken')
#             return redirect(reverse('user_mgr:signUp'))
#         else:
#             if user_reg_form.is_valid():
#                 #print rp['email'] + '\n\n'
#                 username   = user_reg_form.cleaned_data.get('username')
#                 email      = user_reg_form.cleaned_data.get('email')
#                 first_name = user_reg_form.cleaned_data.get('first_name')
#                 last_name  = user_reg_form.cleaned_data.get('last_name')
#                 password   = user_reg_form.cleaned_data.get('password')
#                 user       = User.objects.create(username = username, first_name = first_name, last_name = last_name, email = email,)
#                 user.set_password(password)
#                 user.save()
#                 if user:
#                     #messages.success(request, 'Your account details have been saved')
#                     unique_token  = get_random_string(length=32)
#                     profile       = UserProfile.objects.create(user=user, confirm_key=unique_token)
#                     profile_saved = profile.save()
#                     #print settings.EMAIL_HOST_USER
#                     if profile:
#                         try:
#                             subject      = 'HackPart Account Confirmation'
#                             #message      = "Thank you for signing up on the hackparty platform. Please click on the link above to confirm your account: " + update_url
#                             from_email   = settings.EMAIL_HOST_USER
#                             to_email     = [email, from_email]
#                             domain = get_current_site(request).domain
#                             ctx = { 'username':username, 
#                                     'domain':domain,
#                                     'unique_token': unique_token,  }
#                             print 'am here'
#                             message = render_to_string('user_mgr/activate_email.html', ctx, context_instance=RequestContext(request))
#                             print 'hello'
#                             # email = EmailMessage(subject, message, to=[toemail])
#                             # email.send()
                            
#                             send_mail(subject, message, from_email, to_email, fail_silently=True,)
#                             print 'whats up'
#                             # text_content = "Thank you for signing up on the hackparty platform. Please click on the link below to confirm your account: "
                            
#                             # html_content = "http://" + domain + "/user/confirmation/" + unique_token
#                             # msg = EmailMultiAlternatives(subject, text_content, from_email, to_email,)
#                             # msg.attach_alternative(html_content, "text/html")
#                             # msg.send()
#                             # messages.success(request, 'Your account details have been saved')
#                             return render(request, 'user_mgr/success.html', {'username': username})
#                         except:
#                             messages.debug(request, 'Your account details may not have been saved correctly')
#                             return render(request, 'user_mgr/unsuccessful.html', {'username': username})
#                 else:
#                     messages.warning(request, 'something went wrong acount not created!! please try again!')
#             else: 
#                 #context['reg_form'] = RegistrationForm(data = request.POST)
#                 messages.warning(request, 'something went wrong acount not created!! please try again!')
#                 return render(request, 'user_mgr/signup.html')
#     return redirect(reverse( 'user_mgr:signUp'))   


   
