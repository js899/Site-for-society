from django import forms
from dashboard.models import Event, Participant, Click
import datetime
from datetime import date, datetime
from .models import *


class createEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
    
class registerForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = "__all__"



class DetailForm(forms.ModelForm):
    eventName = forms.CharField(max_length=30)
    body = forms.CharField(max_length=245, label="Event Description")
    class Meta:
        model = Click
        fields = ('eventName', 'body',)


class ClicksForm(forms.ModelForm):
#    images = forms.FileField(label='Image')
    eventName = forms.CharField(max_length=30)
    body = forms.CharField(max_length=245, label="Event Description")
    images = forms.ClearableFileInput(attrs={'multiple': True})
    class Meta:
        model = Click
#        fields = ('images',)
        fields = "__all__"



# class deleteEventForm(forms.Form):
#     eventName = forms.CharField(required = True,  max_length=30)


# class attendanceForms():
#     class class Meta:
#         model = Attendance
#         fields = "__all__"



# Uploading Images In Gallery

class GalleryForm(forms.ModelForm): 

	class Meta: 
		model = Gallery 
		fields = ['name', 'event_Main_Img'] 

