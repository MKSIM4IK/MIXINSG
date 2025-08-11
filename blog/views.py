from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .mixins import (
    TitleMixin, ContentMixin, AuthorMixin, DateMixin,
    SummaryMixin, TagMixin, CategoryMixin, StatusMixin,
    CommentMixin, RatingMixin
)

class PostListView(TitleMixin, ContentMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(AuthorMixin, DateMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.htm'
    context_object_name = 'post'

class PostCreateView(SummaryMixin, TagMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.htm'
    success_url = reverse_lazy('post_list')

class PostUpdateView(CategoryMixin, StatusMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.htm'
    success_url = reverse_lazy('post_list')

class PostDeleteView(CommentMixin, RatingMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_confirm_delete.htm'
