from django.contrib.auth import login, logout, authenticate 
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm, EditForm
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
        
    def get(self, request):
        data = Articles.objects.all()
        if request.user.is_authenticated:        
            return render(request,'users/homepage.html', {'data': data})
        else:            
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


class ShowProfileView(TemplateView):
        
    model = CustomUser
    template_name = 'users/userprofile.html'

    def get_context_data(self, *args, **kwargs):

        users = CustomUser.objects.all()
        context = super(ShowProfileView,self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])    
        context['page_user'] = page_user

        return context


class EditUserView(TemplateView):

    def get(self, request, pk):
        form = EditForm()
        users = CustomUser.objects.all()        
        
        page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])    
        context = {
                'form': form,
                'page_user': page_user
            }
 
        return render(request, "users/edituser.html",context)

    def post(self, request, pk):
        data = CustomUser.objects.all()
        form = EditForm(request.POST)
        if form.is_valid():            
            form.save()       
            return redirect("users:homepage")  
        else:
            form = form = RegisterForm(request.POST)
            return render(request, "users/edituser.html", {"form":form})
        


