from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Advertisement, Tag
from .forms import BlogForm, AdvertisementForm
from users.models import User, Profiles


def blogs(request):
    bl = Blog.objects.all()
    adv = Advertisement.objects.all()
    context = {'blogs': bl, 'advertisement': adv}
    return render(request, 'blogs/blogs.html', context)


def blog(request, pk):
    blog_obj = Blog.objects.get(id=pk)
    context = {'blog': blog_obj}
    return render(request, 'blogs/single-blog.html', context)


@login_required(login_url='login')
def create_blog(request):
    profile = request.user.profile
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = profile
            blog.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'blogs/form-template.html', context)


@login_required(login_url='login')
def update_blog(request, pk):
    profile = request.user.profiles
    bl = profile.blog_set.get(id=pk)
    form = BlogForm(instance=bl)

    if request.method == 'POST':
        # new_tags = request.POST.get('tags').replace(',', ' ').split()
        form = BlogForm(request.POST, request.FILES, instance=bl)
        if form.is_valid():
            # for tag in new_tags:
            #     tag, created = Tag.objects.get_or_create(name=tag)
            #     bl.tags.add(tag)
            bl.save()

            return redirect('account')

    context = {'form': form, 'blog': bl}
    return render(request, 'blogs/form-template.html', context)


@login_required(login_url='login')
def update_advertisement(request, pk):
    profile = request.user.profiles
    advertisement = profile.advertisement_set.get(id=pk)
    form = AdvertisementForm(instance=advertisement)

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)
        if form.is_valid():
            advertisement.save()

            return redirect('account')

    context = {'form': form, 'advertisement': advertisement}
    return render(request, 'blogs/form-advertisement.html', context)


def about(request):
    return render(request, 'blogs/about.html')

