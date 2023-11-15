from django.shortcuts import render
from django.views.generic import ListView
from a1.models import Post

# Create your views here.
class Post_list_view(ListView):
    model = Post
    template_name = 'home.html'