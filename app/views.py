from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def postdetails(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'details.html', {'post':post})


def createpost(request):
    if request.method == "POST":
        title = request.POST.get("title")
        slug = request.POST.get("slug")
        content = request.POST.get("content")
        author = request.user

        Post.objects.create(title=title, slug=slug, content=content, author=author)
        return redirect('home') 
    return render(request, 'create.html')