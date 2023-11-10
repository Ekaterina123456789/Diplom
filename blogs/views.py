from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm


def blogs(request):
    bl = Blog.objects.all()
    context = {'blogs': bl}
    return render(request, 'blogs/blogs.html', context)


def blog(request, pk):
    blog_obj = Blog.objects.get(id=pk)
    context = {'blog': blog_obj}
    return render(request, 'blogs/single-blog.html', context)


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = BlogForm()
        context = {'form': form}
        return render(request, 'blogs/form-template.html', context)
