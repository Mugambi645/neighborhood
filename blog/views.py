from django.shortcuts import render
from .models import BlogPost,Comment
# Create your views here.
def blogs(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')
    return render(request, "blog.html", {'posts':posts})
