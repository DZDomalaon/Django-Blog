from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('homepage/', views.homepage_form, name='homepage'),
    path('register/', views.RegisterView.as_view(), name='register'),    
]