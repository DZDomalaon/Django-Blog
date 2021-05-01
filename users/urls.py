from django.views.generic import TemplateView
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('homepage/', views.HomePageView.as_view(), name='homepage'),
    path('register/', views.RegisterView.as_view(), name='register'),    
]