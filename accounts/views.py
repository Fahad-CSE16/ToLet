from django.db.models import Q
#basic import
from django.shortcuts import render, HttpResponse,redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.views.generic import View
import time
#Userlogin signup, import
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm,ContactForm,UserProfileForm,UserUpdateForm

def registrationview(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request, 'Registration Successfull!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="accounts/login.html",
                  context={'form': form})

def logoutview(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home')
def changepassview(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Has changed successfully!')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/changepass.html', {'form': form})
def contactview(request): 
    if request.method == 'POST':
        form= ContactForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully Sent.')
            return redirect('home')
    else:
        form = ContactForm() 
        
    context = {
            'form':form,
            }
    return render(request, 'accounts/contact_us.html',context )
from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name='home.html'
from .models import UserProfile
def userprofile(request):
    userp = UserProfile.objects.filter(user=request.user)
    query = request.user
    return render(request, 'accounts/userprofile.html', {'userp': userp})

def updateprofile(request):
    try:
        instance = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        instance = None
    if request.method == 'POST':
        if instance:
            p_form = UserProfileForm(request.POST, request.FILES, instance=instance)
        else:
            p_form = UserProfileForm(request.POST, request.FILES)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            profile_obj = p_form.save(commit=False)
            profile_obj.user = request.user
            profile_obj.save()
            email = u_form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists() and request.user.email != email:
                messages.warning(
                    request, 'Your Provided email is already in Use in another profile.')
                return redirect('updateprofile')
            elif request.user.email == email:
                u_form.save()
            messages.success(request, 'Successfully updated.')
            return redirect('userprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=instance)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'accounts/updateprofile.html', context)

