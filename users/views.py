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
    
    template_name = 'users/userprofile.html'

    def get_context_data(self, *args, **kwargs):
        #import pdb; pdb.set_trace()
        post_data = Articles.objects.filter(owner=self.request.user).order_by('-date_created')
        context = super(ShowProfileView,self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])    
        context = {
                'post_data': post_data,
                'page_user': page_user,
            }

        return context


class EditUserView(TemplateView):

    def get(self, request, **kwargs):
        page_user = get_object_or_404(CustomUser, **kwargs)          
        form = EditForm(instance=request.user)                      
        context = {
                'form': form,
                'page_user': page_user
            }        
        return render(request, "users/edituser.html",context)

    def post(self, request, *args, **kwargs):    
                          
        initial_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
            
        form = EditForm(request.POST, instance=request.user, initial=initial_data) 
        page_user = get_object_or_404(CustomUser, **kwargs)              
        if form.is_valid():                         
            update_user = form.save(commit=False)
            update_user.save()                             
            return redirect("users:profile", request.user.id)  
        else:
            form = EditForm(request.POST,  initial=initial_data)        
            return render(request, "users/edituser.html", {'form':form, 'page_user':page_user})
        


