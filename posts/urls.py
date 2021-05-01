from django.views.generic import TemplateView
from django.urls import path
from . import views 

app_name = 'posts'
urlpatterns = [
    path('addpost/', views.AddArticleView.as_view(), name='addpost'),  

]