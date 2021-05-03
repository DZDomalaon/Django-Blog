from django.shortcuts import render, redirect, get_object_or_404, Http404
from .forms import AddArticleForm, EditArticleForm, ArticleCommentsForm
from django.views.generic import TemplateView
from .models import Articles

# Create your views here.

class ArticleView(TemplateView):

    def get(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            data = get_object_or_404(Articles, **kwargs)        
            return render(request, "posts/postpage.html",  {'data':data})
        else:
            return redirect('users:login')
    
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

    def put(request, *args, **kwargs):    

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
                return redirect('users:homepage')
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
                raise Http404("You are not allowed to delete this article.")
        else:
            return redirect('users:login')




class AddCommentView(TemplateView):

    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            form = ArticleCommentsForm()
            return render(request, "users/login.html", {"form":form})
        else:
            return redirect('users:login')

    def post(self, request, *args, **kwargs):

        form = ArticleCommentsForm(request.POST)
        if form.is_valid():            
            post_data = Articles.objects.get(**kwargs)
            create_comment = form.save(commit=False)
            create_comment.article = post_data.id
            form.save()
            return redirect('users:homepage')
        else:
            return render(request, self.template_name, {'form':form})
