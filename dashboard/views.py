#from django.contrib.auth import logout
# Send Newsletter
import smtplib
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth import logout as lgout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from dashboard.forms import createEventForm
from django.contrib import messages
#from django.views.generic import TemplateView
from dashboard.models import Event, Participant, Click
from newsletters.models import NewsletterUser
from dashboard.forms import registerForm
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.forms.models import modelformset_factory
from .forms import *

import datetime 
import datetime

# Create your views here.

def logout(request):
    if request.method == 'POST':
        lgout(request)
        return HttpResponseRedirect('frontpage:index')

# def check():
#     return redirect('frontpage')


def EventPage(request):
    d = datetime.date.today()
    t = datetime.datetime.now().time()
    dt = datetime.datetime.combine(d, t)
    event = Event.objects.last()
    till_date = event.date
    till_time = event.time
    till_date_time = datetime.datetime.combine(till_date, till_time)

    if request.method == 'POST':
        events = Event.objects.all()
        form = registerForm(request.POST)
        args = {'events':events, 'form':form }
        if(till_date_time > dt):
            if form.is_valid():
                form.save(request.POST)
                messages.success(request, "Thank you for registering. See you at the event.")
                return HttpResponseRedirect('')
        else:
            messages.warning(request, "Online registrations are closed now. If you still want to participate, you can get yourself registered at the venue. Thank You.")
            return HttpResponseRedirect('')
        return render(request, "frontpage/events.html", args)
    else:
        events = Event.objects.all()
        register = registerForm()
        args = {'events':events, 'form':register}
        return render(request, "frontpage/events.html", args)


@login_required(login_url='frontpage')
def dash(request):
    events = Event.objects.all()
    if request.method == 'POST':
        form = createEventForm(request.POST, request.FILES)
        args = {'form':form , 'events':events}
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('')
        return render(request, 'dashboard/index.html',args)
    else:
        form = createEventForm()
        args = {'form':form , 'events':events}
        return render(request, 'dashboard/index.html',args)

@login_required(login_url='frontpage')
def attendance(request, id = None):
    participant_attendance_formset = modelformset_factory(Participant, form = registerForm)
    formset = participant_attendance_formset(request.POST or None)
    if formset.is_valid():
        instances = formset.save(commit = False)
        for instance in instances:
            instance.user = request.user
            instance.save()

    args = {'formset':formset}
        
    return render(request, 'dashboard/attendance.html', args)



# @login_required(login_url='frontpage')
# def deleteEventandParticipants(request, event_name):
#     name = Event.objects.get(name = event_name)
#     if request.method == "POST":
#         del_form = deleteEventForm(request.POST)
#         if del_form.is_valid():


@login_required(login_url='frontpage')
def addEventClicks(request):
    ImageFormSet = modelformset_factory(Click, form = ClicksForm, extra=2)
    if request.method == 'POST':
        detailForm = DetailForm(request.POST)
        formset_image = ImageFormSet(request.POST, request.FILES,
                        queryset = Click.objects.none())
        if detailForm.is_valid() and formset_image.is_valid():
            detail_form = detailForm.save(commit = False)
            detail_form.save()

            for form in formset_image.cleaned_data:
                image = form['images']
                photo = Click(images = image)
                #photo = Click(post = detail_form, images = image)
                photo.save()
        
        else:
            print(detailForm.errors, formset_image.errors)
    else:
        detailForm = DetailForm
        formset_image = ImageFormSet(queryset = Click.objects.none())
        args = {'detailForm': detailForm, 'formset': formset_image}
        return render(request, 'dashboard/attendance.html', args,
                )#context_instance = RequestContext(request))
