from django.db import models

# Create your models here.

#Uploading Images In Gallery    
class Gallery(models.Model): 
    name = models.CharField(max_length=50) 
    event_Main_Img = models.ImageField(upload_to='images/') 
    
    def __str__(self):
    	return self.name
