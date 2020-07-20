from django.db import models

# Create your models here.
class Member(models.Model):
    email = models.EmailField(blank = False, max_length=254, unique = True, primary_key = True)
    password = models.CharField(blank=False, max_length=32)

    def __str__(self):
        return self.email