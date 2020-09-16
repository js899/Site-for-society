from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import Gallery
# Create your views here.

def show_gallery(request):
    return render(request, 'gallery/index.html')
    
# Uploading Images In Gallery 
def event_image_view(request): 

	if request.method == 'POST': 
		form = GalleryForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return HttpResponse("Successfully Uploaded!!!") 
	else: 
		form = GalleryForm() 
	return render(request, 'gallery/event_image_form.html', {'form' : form}) 
