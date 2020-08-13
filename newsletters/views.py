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



# Sending PDF For Newsletter
@login_required(login_url='frontpage')
def show_newsletter(request):
    form = NewsletterUploadForm()
    args = {'form':form}
    if form.is_valid():
        form.save(request.POST)
        messages.success(request, "Sent !")
        return HttpResponseRedirect('')
    else:
        return render(request, "dashboard/pdf_upload.html", args)

@login_required(login_url='frontpage')
def pdf_view(request): 
    if request.method == 'POST':
        # mail=smtplib.SMTP('smtp.gmail.com',587)
        # mail.ehlo()
        # mail.starttls()
        # mail.login('csigndec1@gmail.com','CsiGndec1@')
        # mail_list = NewsletterUser.objects.filter().values_list("email", flat=True)
        # for i in range(len(mail_list)):
        #     mail.sendmail('csigndec1@gmail.com',mail_list[i],f'Subject: {request.POST.get("subject")}\n\n'+request.POST.get('message'))
        # mail.quit()
        # return redirect('success')
        mail_list = NewsletterUser.objects.filter().values_list("email", flat=True)
        docform = NewsletterUploadForm(request.POST, request.FILES)
        if docform.is_valid():
            docform.save(request.POST, commit=True)
            df = NewsletterDoc.objects.last()
            for i in range(len(mail_list)):
                # send_mail(
                #     'Monthly Magazine', #subject
                #     'e-Magazine for CSI Magazine subscribers. To unsubscribe click here...',    #body
                #     'csigndec1@gmail.com',  #from
                #     mail_list[i],   #to
                #         #attachment
                #     fail_silently=False,    #True when deploy
                # )
                email = EmailMessage(
                    df.subject, df.message, 'csigndec1@gmail.com', mail_list)
                #email.attach_file(df.pdf)
                try:
                    attachment = df.pdf
                    email.attach(attachment.name, attachment.read(), attachment.content_type)
                    email.send()
                except Exception as e:
                    print(str(e))
            messages.success(request, "Sent !")
            #return redirect('success')
            return HttpResponseRedirect('')
        else:
            return render(request, 'dashboard/sending_newsletter.html')