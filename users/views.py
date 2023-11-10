from django.shortcuts import render
from .models import Profiles, Advertisement


def profile(request):
    users = Profiles.objects.all()
    context = {'profiles': users}
    return render(request, 'users/index.html', context)


def advertisement(request):
    advert = Advertisement.objects.all()
    context = {'advertisement': advert}
    return render(request, 'blogs/blogs.html', context)
