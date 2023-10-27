from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog


def blogs(request):
    bl = Blog.objects.all()
    context = {'blogs': bl}
    return render(request, 'blogs/blogs.html', context)


def blog(request, pk):
    blog_obj = Blog.objects.get(id=pk)
    context = {'blog': blog_obj}
    return render(request, 'blogs/single-blog.html', context)
