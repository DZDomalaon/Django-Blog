from django.contrib.auth import login, logout, authenticate
from django.forms import ModelForm
from .models import CustomUser
from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label="Email", required=True)
    password = forms.CharField(label="Password",widget=forms.PasswordInput, required=True)

    field = ('email', 'password')
    def auth(self, request):        
        auth_email = self.cleaned_data.get('email')   
        pword = self.cleaned_data.get('password')
        return authenticate(request, username=auth_email, password=pword)

class RegisterForm(forms.ModelForm):
    firstname = forms.CharField(label="First name", required=True)
    lastname = forms.CharField(label="Last name", required=True)
    email = forms.CharField(label="Email", required=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)


    class Meta:
        model = CustomUser
        fields = ('firstname','lastname','email', 'password')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2