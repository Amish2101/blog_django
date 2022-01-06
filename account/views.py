from django.contrib.auth import login, authenticate, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from .forms import newUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def Register(request):
    if request.method == 'POST':
        form = newUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"successfully registration")
            return redirect("blog:home")
        messages.error(request, "unsuccessful registration")
    form = newUser()
    return render(request=request, template_name='account/register.html', context={'form':form})


def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"loggin { username } ")
                return redirect("account:bio")
            else:
                messages.error(request, "invalid username and password")
        else:
            messages.error(request, "invalid username and password")
    form = AuthenticationForm()
    return render(request, "account/login.html", {'login_form':form})

@login_required
def bio(request):

    user = User.objects.get(id = request.user.id)
    print(user)
    return render(request, 'account/bio.html', {'user':user})

@login_required
def Logout(request):
    logout(request)
    return redirect("blog:home")