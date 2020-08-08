from django.contrib import admin
from dashboard.models import Event, Participant, Click, Gallery, Newsletter

# Register your models here.
admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Click)
admin.site.register(Gallery)
admin.site.register(Newsletter)
