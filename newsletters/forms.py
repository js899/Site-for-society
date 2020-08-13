from django import forms
from .models import NewsletterUser, NewsletterDoc
#from crispy_forms.helper import FormHelper

class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email

class NewsletterUploadForm(forms.ModelForm):
    class Meta:
        model = NewsletterDoc
        fields = "__all__"