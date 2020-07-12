from django.contrib import admin

from .models import Author, Category, Post, Comment, PostView,HomePage,Galary

admin.site.register(Author)
admin.site.register(HomePage)
admin.site.register(Galary)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)