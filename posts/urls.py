from django.urls import path
from . import views 

app_name = 'posts'
urlpatterns = [
    path('addpost/', views.ArticleView.post, name='addpost'),  
    path('<int:pk>/postpage', views.ArticleView.get, name='postpage'),
    path('<int:pk>/postpage/editpost', views.ArticleView.put, name='editpost'),
    path('<int:pk>/postpage/deletepost', views.ArticleView.delete, name='deletepost'),
]