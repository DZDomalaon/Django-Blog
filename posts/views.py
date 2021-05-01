from django.shortcuts import render, redirect
from .forms import AddArticleForm
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

