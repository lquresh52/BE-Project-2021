from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout, authenticate
from .models import UserRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from studentDashboard.views import dashboard
from adminPanel.views import teacherHome,questionForm,questionList

def index(request):
    return render(request, 'accounts/index.html')

def signUp(request):
    if request.method == 'POST':
        print("Arra")
        if request.POST.get('password') ==request.POST.get('confirmPassword'):
            try:
                user = User.objects.get(email= request.POST.get('email'))
                print("TRY WALA UDSER _______________",user)
                print("Galat")
                errormsg = 'Account Already Exist.'
                return render(request,'accounts/index.html',{'signUpModel':'true', 'errormsg':errormsg})
            except:
                user = User.objects.create_user(username=request.POST.get('email'), email=request.POST.get('email'),password=request.POST.get('password'), first_name=request.POST.get('firstName'), last_name=request.POST.get('lastName'))
                phone_number = request.POST.get('phoneNumber')
                user.is_active = False
                user.save()
                print(request.POST.get('collegeName'),request.POST.get('branchSelect'), request.POST.get('yearSelect'))
                actualUserRegister = UserRegistration(user=user, phone_number=phone_number,college_name = request.POST.get('collegeName'),branch = request.POST.get('branchSelect'),year = request.POST.get('yearSelect'))
                actualUserRegister.save()
                print("Registered")
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string(
                    'accounts/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = user.email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                messages.success(request, f'Registration Successfull!! We have sent you a mail. Please click on the link provided in the mail to activate your account.')
                return redirect('index')
                # user = authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
                # auth.login(request, user)
                # if user.is_authenticated:
                #     print("Logged In")
                #     return redirect(dashboard)
        return render(request, 'accounts/index.html')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, f'Thank you for your email confirmation. Now you can login into your account.')
        return redirect('index')
    else:
        messages.error(request, f'Activation link is invalid!')
        return redirect('index')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        messages.success(request, f'------------------')
        return render(request, 'accounts/password_reset_done.html', {'uid': uidb64})
    else:
        messages.error(request, f'Activation link is invalid!')
        return redirect('index')        

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            print(user.userregistration.phone_number)
            user = authenticate(request,username=username,password=password)
            auth.login(request, user)
            print("-------------------------------------")
            print(user.userregistration.isTeacher)
            if user.userregistration.isTeacher:
                print("Teacher Logged In")
                return redirect(teacherHome)
            else:
                if user.is_authenticated:
                    print("Logged In")
                    return redirect(dashboard)
                    print("Allow user to login")
        except:
            print("User not exist")
            try:
                user = User.objects.get(username=username)
                if user.is_active == False:
                    errormsg = 'Email Not Verified'
                else:
                    errormsg = 'Email or Password Incorrect'
            except:        
                errormsg = 'User Does Not Exists'
            
            return render(request, 'accounts/index.html', {'loginModel':'true', 'errormsg':errormsg})
    return render(request, 'accounts/index.html', {'loginModel':'true'})        


def logout_user(request):
    auth.logout(request)
    print("LogOut")
    return redirect(index)

def password_reset(request):
    if request.method == 'POST':
        myEmail = request.POST.get('email')
        try:
            user = User.objects.get(email=myEmail)
            print('---------------------------------')
            print(user.pk)
            
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            print('********')
            print(current_site.domain)
            print("-----Here------")
            message = render_to_string(
                'accounts/password_reset_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            print(message)
            print('------Now Here--------')
            to_email = user.email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            print('Mail Sent')
            messages.success(request, f'Registration Successfull!! We have sent you a mail. Please click on the link provided in the mail to activate your account.')
            return redirect('password-reset')
            if user.is_active == False:
                messages.error(request, f'You have not verified your mail.')
                return render(request, 'accounts/password_reset.html') 
            else:
                messages.error(request, f'You do not have an account registered for the given email.')
                return render(request, 'accounts/password_reset.html')      
        except:
            print("Invalid---------------------------------")
            messages.error(request, f'You do not have an account registered for the given email.')
            return render(request, 'accounts/password_reset.html')
    else:    
        return render(request, 'accounts/password_reset.html')   

def password_reset_completed(request, uidb64):
    print('###################')
    print(uidb64)
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        print(user)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None:
        password = request.POST.get('password')
        user.set_password(password)
        user.save()
        print('Pasword Saved')    
    return HttpResponse('Completed')
               