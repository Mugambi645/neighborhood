from django.shortcuts import render,redirect
from .models import BlogPost,Comment
from .forms import BlogPostForm
# Create your views here.
def blogs(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')
    return render(request, "blog.html", {'posts':posts})

def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return redirect('blog:blogs')  
    else:
        form=BlogPostForm()
    return render(request, "add_blogs.html", {'form':form})


def blogs_comments(request, id):
    post = BlogPost.objects.get(id = id)
    return render(request, "blog_comments.html", {'post':post}) 

