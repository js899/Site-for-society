from django.db import models

# Create your models here.
class NewsletterUser(models.Model):
    email = models.EmailField(primary_key = True)

    def __str__(self):
        return self.email
class NewsletterDoc(models.Model):
    subject = models.CharField(blank = False, max_length=100)
    message = models.CharField(blank = False, max_length=200)
    pdf = models.FileField(upload_to='documents/event_bg/',blank=False)

    def __str__(self):
        return self.pdf.name