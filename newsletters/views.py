from django.contrib import messages
from django.shortcuts import render
from .models import NewsletterUser
from django.conf import settings
from .forms import NewsletterSignupForm
from django.core.mail import send_mail#, send_mass_mail
# Create your views here.
def newsletter_signup(request):
    form = NewsletterSignupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email = instance.email).exists():
            messages.warning(request,'Your email already exists in the database',
            'alert alert-warning alert-dismissible')
        else:
            instance.save()
            messages.success(request,'Thanks for subscribing. You will now receive an acknowledgement email.',
            'alert alert-success alert-dismissible')
            subject = 'Welcome to CSI Newsletter.'
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            signup_message = """Thanks for subscribing to CSI e-magazine. You can unsubscribe at http://127.0.0.1:8000/newsletter_unsubscribe/"""
            send_mail(subject = subject, from_email = from_email, recipient_list = to_email, message = signup_message, fail_silently= False)

    context = {'form': form, 
    #'messages':messages,           
    }
    template = 'newsletters/sign_up.html'
    return render(request, template, context)

def newsletter_unsubscribe(request):
    form = NewsletterSignupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email = instance.email).exists():
            NewsletterUser.objects.filter(email = instance.email).delete()
            messages.success(request,
                            'See you soon.', 
                            'alert alert-success alert-dismissible')
            subject = 'Sorry to see you go.'
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            signup_message = """Please let us know if there is any issue with our service. Till then you won't receive any updates. You can however subscribe at http://127.0.0.1:8000/newsletter_signup/"""
            send_mail(subject = subject, from_email = from_email, recipient_list = to_email, message = signup_message, fail_silently= False)

        else:
            messages.warning(request,
                            'Sorry, your email is not in our database.', 
                            'alert alert-warning alert-dismissible')
    
    context = {'form': form,
    #'messages':messages,
    }
    template = 'newsletters/unsubscribe.html'
    return render(request, template, context)
