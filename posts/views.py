from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'


class PostDraftListView(ListView):
    model = Post
    template_name = 'posts/draft_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status__name__iexact='draft')


class PostArchivedListView(ListView):
    model = Post
    template_name = 'posts/archived_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status__name__iexact='archived')


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'sub_title', 'body', 'status']

    # Sets the author as the logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    fields = ['title', 'sub_title', 'body', 'status']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts')