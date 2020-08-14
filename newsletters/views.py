from django.contrib import messages
from django.shortcuts import render, redirect
from .models import NewsletterUser
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
   
def subscribe(request):
    if request.method == "POST":
        n = NewsletterUser(email=request.POST.get('email'))
        if ('@' in str(n) ) and ( ('.com' or '.in') in str(n) ):
            n.save()
            return render(request, "frontpage/index.html")
        else:
            return render(request, "frontpage/index.html")

def success(request): 
	return HttpResponse('Successfully Sent!!!') 



# Sending PDF For Newsletter
@login_required(login_url='frontpage')
def show_newsletter(request):
    return render(request, 'dashboard/pdf_upload.html')
    

@login_required(login_url='frontpage')
def pdf_view(request): 
    if request.method == 'POST':
        subject = request.POST.get('subject','')
        message = request.POST.get('message')
        mail_list = NewsletterUser.objects.filter().values_list("email", flat=True)
        email = EmailMessage(subject, message, 'csigndec1@gmail.com', mail_list)
        email.content_subtype = 'html'
        
        pdf = request.FILES['file']
        email.attach(pdf.name, pdf.read(), pdf.content_type)
        email.send()
        return redirect('success')
    else:
        return render(request, "dashboard/index.html")
