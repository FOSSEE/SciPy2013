from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from scipy.forms import UserLoginForm, UserRegisterForm, UserProfileForm, DocumentUploadForm

# User Login View
def user_login(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponse("Not active")
            else:
                return HttpResponse("Invalid username or password")
        else:
            form = UserLoginForm()

        next = '/accounts/upload-document/'
        if 'next' in request.GET:
            next = request.GET['next']

        context = {}
        context.update(csrf(request))
        context['form'] = form
        context['next'] = next
        return render_to_response('login.html', context)
    else:
        return HttpResponseRedirect('/accounts/upload-document')

# User Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/2013')

# User Register View
def user_register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid:
                form.save()
            return HttpResponseRedirect('/accounts/upload-document')
        else:
            form = UserRegisterForm()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        return render_to_response('register.html', context)
    else:
        return HttpResponseRedirect('/accounts/upload-document')

# User Profile View
def user_profile(request):
    if request.user.is_authenticated():
        context = {}
        context.update(csrf(request))
        context['form'] = UserProfileForm(instance=request.user)
        return render_to_response('profile.html', context)
    else:
        return HttpResponseRedirect('/accounts/login?next=/accounts/profile')

# Document Upload View
@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.verified = False
            data.save()
            return HttpResponseRedirect("/2013/call-for-proposals/?status=up")
        else:
            context = {}
            context.update(csrf(request))
            context['form'] = form
            return render_to_response('upload-document.html', context)
    else:
        form = DocumentUploadForm()
        
    context = {}
    context.update(csrf(request))
    context['form'] = DocumentUploadForm()
    return render_to_response('upload-document.html', context)
    
    
    
    
    
