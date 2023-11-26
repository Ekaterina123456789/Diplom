from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Advertisement, Tag
from .forms import BlogForm, AdvertisementForm, ReviewForm
from .utils import search_blogs
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from users.models import User, Profiles


def blogs(request):
    page = request.GET.get('page')
    results = 3

    bl, search_query = search_blogs(request)
    adv = Advertisement.objects.all()

    paginator = Paginator(bl, results)
    try:
        bl = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        bl = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        bl = paginator.page(page)

    left_index = int(page) - 2
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 3
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {'blogs': bl,
               'advertisement': adv,
               'search_query': search_query,
               'paginator': paginator,
               'custom_range': custom_range}
    return render(request, 'blogs/blogs.html', context)


def blog(request, pk):
    form = ReviewForm()
    blog_obj = Blog.objects.get(id=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.blog = blog_obj
        review.owner = request.user.profiles
        review.save()

        messages.success(request, 'Ваш отзыв успешно опубликован!')
        return redirect('blog', pk=blog_obj.id)

    context = {'blog': blog_obj, 'form': form}
    return render(request, 'blogs/single-blog.html', context)


@login_required(login_url='login')
def create_blog(request):
    profile = request.user.profiles
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
def delete_blog(request, pk):
    profile = request.user.profiles
    bl = profile.blog_set.get(id=pk)

    if request.method == 'POST':
        bl.delete()
        return redirect('account')

    context = {'blog': bl}
    return render(request, 'blogs/delete.html', context)


# перенести create_advertisement, update_advertisement и delete_advertisement в приложение user
@login_required(login_url='login')
def create_advertisement(request):
    profile = request.user.profiles
    form = AdvertisementForm()

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = form.save(commit=False)
            adv.owner = profile
            adv.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'blogs/form-advertisement.html', context)


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


@login_required(login_url='login')
def delete_advertisement(request, pk):
    profile = request.user.profiles
    adv = profile.blog_set.get(id=pk)

    if request.method == 'POST':
        adv.delete()
        return redirect('account')

    context = {'advertisement': adv}
    return render(request, 'blogs/delete.html', context)


def autor(request):

    return render(request, 'blogs/autor.html')


def history(request):

    return render(request, 'blogs/history.html')


def results(request):

    return render(request, 'blogs/results.html')
