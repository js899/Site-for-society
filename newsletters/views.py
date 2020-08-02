from django.contrib import messages
from django.shortcuts import render
from .models import NewsletterUser
from django.conf import settings

# Create your views here.
   
def subscribe(request):
    if request.method == "POST":
        n = NewsletterUser(email=request.POST.get('email'))
        if '@gmail.com' in str(n):
            n.save()
            return render(request, "frontpage/index.html")
        else:
            return render(request, "frontpage/index.html")
