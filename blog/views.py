from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('date_posted')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# class based views are powerful because we do not have to manually create the forms
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # default <app>/<model>_<viewtype>.html blog/post_list.html
    context_object_name = 'posts' # by default, django calls the model object_list
    ordering = ['-date_posted'] # get_queryset overwrites this!
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # default <app>/<model>_<viewtype>.html blog/post_list.html
    context_object_name = 'posts' # by default, django calls the model object_list
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    # the DetailView expects a pk value to be passed via the url by default
    # otherwise an attribute must be added.

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # before submiting POST request via online form, we need to set author as the currently logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# CreateView and UpdateView uses the same template! blog/post_form.html
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # before submiting POST request via online form, we need to set author as the currently logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # first, get post we are trying to update
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        # first, get post we are trying to update
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
