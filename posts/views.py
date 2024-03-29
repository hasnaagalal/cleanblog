from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView ,CreateView , UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin





def about (request):
    return render (request,'posts/about.html',{'title':"about"})


def contact (request):
    return render (request,'posts/contact.html',{'title':"contact"})


def posts (request):
    return render (request,'posts/posts.html',{'title':"posts"})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    paginate_by=10
    template_name = 'posts/post.html'
    
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/post_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False