from django.shortcuts import render, redirect
from .models import Profiles, User
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def profile(request):
    users = Profiles.objects.all()
    context = {'profiles': users}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profiles.objects.get(pk=pk)
    top_skills = prof.skill_set.exclude(description__exact='')
    other_skills = prof.skill_set.filter(description__exact='')
    context = {
        'profile': prof,
        'top_skills': top_skills,
        'other_skills': other_skills,
    }
    return render(request, 'users/profile.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request,'username does not exists!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'Username or password is incorrect!')

    return render(request, 'users/login.html')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, 'Username was logged out!')
    return redirect('login')
