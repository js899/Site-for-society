from django.contrib import messages
from django.shortcuts import render, redirect
from .models import NewsletterUser, NewsletterDoc
from django.conf import settings
import smtplib
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewsletterUploadForm


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
	return HttpResponse('Successfully Uploaded') 



# Sending Newsletter
@login_required(login_url='frontpage')
def upload_newsletter(request):
    if request.method == 'POST':
        docform = NewsletterUploadForm(request.POST, request.FILES)
        args = {'form':docform}
        if docform.is_valid():
            df = docform.save()
            mail_list = NewsletterUser.objects.filter().values_list("email", flat=True)
            for i in mail_list:
                email = EmailMessage(
                    df.subject, df.message, 'csigndec1@gmail.com', i)
                try:
                    attachment = df.pdf
                    email.attach(attachment.name, attachment.read(), attachment.content_type)
                    email.send(fail_silently=False)
                except Exception as e:
                    messages.warning(request,str(e))
            messages.success(request, "Sent !")
            #return redirect('success')
            return HttpResponseRedirect('')
        else:
            messages.warning(request, "Not sent")
            return HttpResponseRedirect('')
        return render(request, 'dashboard/pdf_upload.html', args)
    else:
        messages.warning(request, "Dafa ho")
        docform = NewsletterUploadForm()
        args = {'form':docform}
        return render(request, 'dashboard/pdf_upload.html', args)

# @login_required(login_url='frontpage')
# def pdf_view(request): 