from django.contrib import admin
from .models import NewsletterUser, NewsletterDoc
# Register your models here.
admin.site.register(NewsletterUser)
admin.site.register(NewsletterDoc)