from django.contrib.auth import login, logout, authenticate 
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages 
from django.http import HttpResponse
from .models import CustomUser



# Create your views here.
class LoginView(TemplateView):

    
    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {"form":form})
        
    def post(self, request):
        form = LoginForm(request.POST) 
             
        if form.is_valid():            
            user = form.auth(request)                    
            if user is not None:
                login(request, user)                             
                return redirect("users:homepage")
                
            else:                   
                form = LoginForm(request.POST)            
                messages.error(request,"Invalid username or password.")
                return render(request, "users/login.html", {"form":form})
        else:
            messages.error(request,"Invalid form")
            return render(request, "users/login.html", {"form":form})
    

def homepage_form(request):        
    if request.user.is_authenticated:        
        return render (request,template_name = 'users/homepage.html')
    form = LoginForm()
    return render(request, "users/login.html", {"form":form})


class RegisterView(TemplateView): 

    def get(self, request):
        form = RegisterForm()
        return render(request=request, template_name="users/register.html", context={"form":form})

    def post(self, request):

        form = RegisterForm(request.POST)
        if form.is_valid():
            test = form.save()
            
            test.set_password(form.cleaned_data.get('password'))            
            username = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')            
            user = authenticate(username=username, password=password)            
            return redirect("users:login")
            
        else:
            form = RegisterForm(request.POST)
            return render(request, "users/register.html", {"form":form})
    

class LogoutView(TemplateView):
    
    def get(self, request):
        logout(request)
        return redirect('users:login')


# class EditView(TemplateView):
#     def get(self, request):

