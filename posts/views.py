from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddArticleForm, EditArticleForm
from django.views.generic import TemplateView
from .models import Articles

# Create your views here.

class AddArticleView(TemplateView):

    template_name = 'posts/addpost.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = AddArticleForm(request.POST)

            return self.render_to_response({
                'form':form,
            })

        else:
            return redirect('users:login')
    
    def post(self, request, *args, **kwargs):
        
        form = AddArticleForm(request.POST)
        if form.is_valid():            
            create_article = form.save(commit=False)
            create_article.owner = request.user      
            form.save()
            return redirect('users:homepage')
        else:
            return render(request, self.template_name, {'form':form})


class EditArticleView(TemplateView):

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            form = EditArticleForm()                  
            page_post = get_object_or_404(Articles, **kwargs)    
            context = {
                    'form': form, 
                    'page_post': page_post,
                                
                }
            return render(request, "posts/editpost.html",context)
        else:
            redirect('users:login')

    def post(self, request, **kwargs):        
        instance = Articles.objects.get(**kwargs)     
        form = EditArticleForm(request.POST, instance=instance)                 
        if form.is_valid():            
            update_article = form.save(commit=False)                        
            update_article.save()
            return redirect('users:homepage')
        else:
            form = EditArticleForm(request.POST, instance=instance)
            return render(request, "posts/editpost.html", {"form":form})


class DeleteArticleView(TemplateView):

    def get(self, *args, **kwargs):
        
        post = get_object_or_404(Articles, **kwargs)
        post.delete()
        return redirect('users:profile')


class ArticlePage(TemplateView):
    template_name = 'posts/postpage.html'

    def get_context_data(self, *args, **kwargs):
    
        data = get_object_or_404(Articles, id=self.kwargs['pk'])
        context = super(ArticlePage,self).get_context_data(*args, **kwargs)   
        context = {
                'data': data,
            }

        return context
