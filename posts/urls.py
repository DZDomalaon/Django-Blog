from django.urls import path
from . import views 

app_name = 'posts'
urlpatterns = [
    path('addpost/', views.ArticleView.post, name='addpost'),  
    path('<int:pk>/postpage', views.ArticleView.get, name='postpage'),
    path('<int:pk>/postpage/addcomment', views.CommentView.post, name='addcomment'),
    path('<int:pk>/postpage/updatecomment', views.CommentView.update_comment, name='updatecomment'),
    path('<int:pk>/postpage/deletecomment', views.CommentView.delete, name='deletecomment'),
    path('<int:pk>/postpage/editpost', views.ArticleView.update_article, name='editpost'),
    path('<int:pk>/postpage/deletepost', views.ArticleView.delete, name='deletepost'),
]