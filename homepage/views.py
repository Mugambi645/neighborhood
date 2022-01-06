from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required 
# Create your views here.
def index(request):
    return render(request, "home/index.html", {})


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    view class to create post
    """
    model = Post
    fields = "__all__"
    template_name = 'hoods/create_hood.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required(login_url='/accounts/login/')
def post(request, pk):
    """
    View to handle post model
    Args:
    Pk - Primary Key,an unique way to identify an object uniquely in relational database systems
    """
    post = Post.objects.get(pk=pk)
    user = request.user
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author= user,description=form.cleaned_data["description"],post=post)
            comment.save()

    comments = Comment.objects.filter(post=post).order_by('-date_posted')
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return self.get(self, request, pk, context)

