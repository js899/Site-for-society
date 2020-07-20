from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(required = True, max_length=100, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    password = forms.CharField(required = True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))