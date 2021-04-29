from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models import CustomUser


class Articles(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    content = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ArticleComments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

class ArticleLikes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)    

    def __str__(self):
        return self.is_liked
    

# class Post(models.Model):
#     STATUS_CHOICES = (
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     )

#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, unique_for_date='publish')
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

#     def __str__(self):
#         return self.title