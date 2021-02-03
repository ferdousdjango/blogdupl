from django.contrib import admin
from blog.models import Post, BlogComment,HomePost

admin.site.register((Post,BlogComment,HomePost))



