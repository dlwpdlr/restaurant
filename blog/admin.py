from django.contrib import admin
from .models import Post, Comment, About

admin.site.register(About)
admin.site.register(Post)
admin.site.register(Comment)
