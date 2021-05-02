from django.views.generic import TemplateView
from django.urls import path
from . import views 

app_name = 'posts'
urlpatterns = [
    path('addpost/', views.AddArticleView.as_view(), name='addpost'),  
    path('<int:pk>/postpage', views.ArticlePage.as_view(), name='postpage'),
    path('<int:pk>/editpost', views.EditArticleView.as_view(), name='editpost'),
    path('<int:pk>/deletepost', views.DeleteArticleView.as_view(), name='deletepost'),
]