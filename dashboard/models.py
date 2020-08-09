from django.db import models
import datetime
from datetime import date, datetime
from django import forms
from django.utils import timezone
# Create your models here.
class Event(models.Model):
    title = models.CharField(blank = False, max_length=20)
    date = models.DateField(blank=False, max_length=15)
    time = models.TimeField(blank=False, max_length=10)
    venue = models.CharField(blank=False, max_length=35, default = 'MBA block')
    image = models.ImageField(upload_to='images/event_bg/',null=True)

    class Meta:
        db_table = 'Event'

    def __str__(self):
        return self.title

class Participant(models.Model):
    BRANCH_CHOICES = (
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EE', 'EE'),
        ('MECH', 'MECH'),
        ('PE', 'PE'),
        ('IT', 'IT'),
        ('CE', 'CE'),
    )

    YEAR_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )

    name = models.CharField(blank = False, max_length=20)
    branch = models.CharField(blank = False, choices = BRANCH_CHOICES, max_length=20)
    year = models.CharField(blank = False, choices = YEAR_CHOICES, max_length=20)
    email = models.EmailField(blank = False, max_length=254, unique = True, primary_key = True)
    present = models.CharField(default = 'No', max_length=10, editable = True, null = True)
#   contact = models.PhoneNumberField(null = False, blank = False, unique = True)
#   eventToParticipateIn = models.CharField(blank = False, max_length=20)

    class Meta:
        db_table = 'Participant'
    
    def __str__(self):
        return self.name

class Click(models.Model):
    eventName = models.CharField(blank = False, max_length=30)
    body = models.CharField(max_length=30, null = True)
    images = models.FileField(upload_to='images/past_events_images/',null=True)

#Uploading Images In Gallery    
class Gallery(models.Model): 
    name = models.CharField(max_length=50) 
    event_Main_Img = models.ImageField(upload_to='images/') 
    
    def __str__(self):
    	return self.name
