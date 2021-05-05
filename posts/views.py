from django.shortcuts import render, redirect, get_object_or_404, Http404
from .forms import AddArticleForm, EditArticleForm, ArticleCommentsForm, ArticleCommentsEditForm
from django.views.generic import TemplateView
from .models import Articles, ArticleComments, ArticleLikes

# Create your views here.

class ArticleView(TemplateView):

    def get(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            page_post = get_object_or_404(Articles, **kwargs)
            post_comment = ArticleComments.objects.all()
            #import pdb; pdb.set_trace()
            form = ArticleCommentsForm()
            context = {
                    'form': form, 
                    'page_post': page_post, 
                    'post_comment': post_comment,
            }
            return render(request, "posts/postpage.html",  context)
        else:
            return render(request, "posts/postpage.html",  context)
    
    def post(request, *args, **kwargs):
        
        template_name = 'posts/addpost.html'
        form = AddArticleForm(request.POST)
        if form.is_valid():            
            create_article = form.save(commit=False)
            create_article.owner = request.user      
            form.save()
            return redirect('users:homepage')
        else:
            return render(request, template_name, {'form':form})

    def update_article(request, *args, **kwargs):

        if request.user.is_authenticated:                     
            page_post = get_object_or_404(Articles, **kwargs)

            initial_data = {
                'title': page_post.title,
                'description': page_post.description,
                'content': page_post.content,
            }                                
            form = EditArticleForm(request.POST or None, instance=page_post, initial=initial_data)               
            context = {
                    'form': form, 
                    'page_post': page_post, 
            }            
            if form.is_valid(): 
                update_article = form.save(commit=False)                        
                update_article.save()
                return redirect('posts:postpage', page_post.id)
            else:
                form = EditArticleForm(request.POST, initial=initial_data)
                return render(request, "posts/editpost.html", context)
        else:
             redirect('users:login')

    def delete(request, *args, **kwargs):
        if request.user.is_authenticated:
            post = get_object_or_404(Articles, **kwargs)
            if request.user.id == post.owner.id:
                post.delete()
                return redirect('users:homepage')
        else:
            return redirect('users:login')


class CommentView(TemplateView):

    def get(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            page_post = get_object_or_404(Articles, **kwargs)            
            #import pdb; pdb.set_trace()
            form = ArticleCommentsForm()
            context = {
                    'form': form, 
                    'page_post': page_post, 
                    'post_comment': post_comment,
            }
            return render(request, "posts/postpage.html",  context)
        else:
            return render(request, "posts/postpage.html",  context)

    def post(request, *args, **kwargs):               
                                
        form = ArticleCommentsForm(request.POST)                
        if form.is_valid():        
            page_post =Articles.objects.get(**kwargs)                
            create_comment = form.save(commit=False)
            create_comment.user = request.user              
            create_comment.article = page_post            
            form.save()
            return redirect('posts:postpage', kwargs.get('pk'))
        else:
            return redirect('posts:postpage', kwargs.get('pk'))

    def update_comment(self, request, *args, **kwargs):
        if request.user.is_authenticated:                     
            for_update_comment = get_object_or_404(ArticleComments, **kwargs)

            initial_data = {
                'comment': post_comment.comment,
            }                                
            updatecommentform = ArticleCommentsEditForm(request.POST, instance=page_post, initial=initial_data)
            context = {
                    'updatecommentform': updatecommentform, 
                    'for_update_comment': for_update_comment,
                    'pk': kwargs.get('pk'),
                }                                       
            if updatecommentform.is_valid():                 
                update_comment = form.save(commit=False)                        
                update_comment.save()
                return redirect('posts:postpage', for_update_comment.article.id)
            else:
                updatecommentform = ArticleCommentsEditForm(request.POST, initial=initial_data)
                return render(request, "posts/postpage.html", context)
                
        else:
             redirect('users:login')

    def delete(request, *args, **kwargs):       
       
        if request.user.is_authenticated:            
            comment = get_object_or_404(ArticleComments, pk=kwargs.get('pk'))
            if request.user.id == comment.user.id:
                comment.delete()
                return redirect('posts:postpage', comment.article.id)
        else:
            return redirect('users:login')