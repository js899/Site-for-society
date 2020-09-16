from django import forms
from .models import *


# Uploading Images In Gallery

class GalleryForm(forms.ModelForm): 

	class Meta: 
		model = Gallery 
		fields = ['name', 'event_Main_Img']
