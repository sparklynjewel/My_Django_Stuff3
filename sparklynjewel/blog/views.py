from django.urls import reverse_lazy
from django.views.generic import ListView, __all__, CreateView, DetailView, DeleteView
from .models import Post
from django.shortcuts import render


# Create your views here.
class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = [
        "cradle"
    ]


class PostDetailView(DetailView):
    model = Post
    fields = [
        "cradle"
    ]


class PostDeleteView(DeleteView):
    model = Post
    fields = [
        "cradle"
    ]
