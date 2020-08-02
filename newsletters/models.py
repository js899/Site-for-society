from django.db import models

# Create your models here.
class NewsletterUser(models.Model):
    email = models.EmailField(primary_key = True)

    def __str__(self):
        return self.email
