from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.db import models
from frontpage.models import Member
from frontpage.forms import LoginForm
from django.contrib.auth import login as memberlogin#, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            memberlogin(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'frontpage/index.html',{'form':form})

#def front(request):
#    return render(request, 'frontpage/index.html')