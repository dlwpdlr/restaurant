from django.contrib import admin
from .models import Post, Comment, About, Map, Gallery

admin.site.register(Gallery)
admin.site.register(About)
admin.site.register(Map)
admin.site.register(Post)
admin.site.register(Comment)
