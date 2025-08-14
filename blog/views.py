from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .mixins import AutoAuthorMixin, AuthorOnlyMixin, SuccessMessageMixin

class PostListView(ListView):
    model = Post
    template_name = 'post_list.htm'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.htm'
    context_object_name = 'post'

class PostCreateView(AutoAuthorMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.htm'
    success_url = reverse_lazy('post_list')
    success_message = "Пост успішно створено!"

class PostUpdateView(AuthorOnlyMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.htm'
    success_url = reverse_lazy('post_list')
    success_message = "Пост успішно оновлено!"

class PostDeleteView(AuthorOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'post_confirm_delete.htm'
