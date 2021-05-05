from django.contrib import admin
from .models import Articles, ArticleComments
# Register your models here.

admin.site.register(Articles)
admin.site.register(ArticleComments)
