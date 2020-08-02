from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def show_gallery(request):
    return render(request, 'gallery/index.html')
