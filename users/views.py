from django.contrib.auth import login, logout, authenticate 
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages 
from .models import CustomUser
from posts.models import Articles



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
    

class HomePageView(TemplateView): 
    # data = Articles.objects.all()     
    # if request.user.is_authenticated:        
    #     return render (request,template_name= 'users/homepage.html', {'data': data})
    # form = LoginForm()
    # return render(request, "users/login.html", {"form":form})
    def get(self, request):
        data = Articles.objects.all()
        return render(request=request, template_name="users/homepage.html", context={"data":data})


class RegisterView(TemplateView): 

    def get(self, request):
        form = RegisterForm()
        return render(request=request, template_name="users/register.html", context={"form":form})

    def post(self, request):

        form = RegisterForm(request.POST)
        if form.is_valid():
            test = form.save()                                 
            username = form.cleaned_data.get('email')            
            # password = form.cleaned_data.get('password')            
            user = authenticate(username=username, password=test.set_password(form.cleaned_data.get('password')))            
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

