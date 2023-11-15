from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Advertisement
from .forms import BlogForm
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
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = BlogForm()
        context = {'form': form}
        return render(request, 'blogs/form-template.html', context)


# def user_profile(request, pk):
#     prof = Profiles.objects.get(pk=pk)
#     top_skills = prof.skill_set.exclude(description__exact='')
#     other_skills = prof.skill_set.filter(description__exact='')
#     context = {
#         'profile': prof,
#         'top_skills': top_skills,
#         'other_skills': other_skills,
#     }
#     return render(request, 'users/profile.html', context)

def about(request):
    return render(request, 'blogs/about.html')

