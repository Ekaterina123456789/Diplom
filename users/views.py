from django.shortcuts import render, redirect
from .models import Profiles, User
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from .utils import search_profiles
from blogs.models import Advertisement


def profile(request):
    users = Profiles.objects.all()
    context = {'profiles': users}
    return render(request, 'users/index.html', context)


def profiles(request):
    users, search_query = search_profiles(request)

    context = {'profiles': users, 'search_query': search_query}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profiles.objects.get(pk=pk)
    top_skills = prof.skill_set.exclude(description__exact='')
    other_skills = prof.skill_set.filter(description__exact='')
    advertisement = Advertisement.objects.all()
    context = {
        'profile': prof,
        'top_skills': top_skills,
        'other_skills': other_skills,
        'advertisement': advertisement,
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

    return render(request, 'users/login_register.html')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User was created successfully!')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occurred during registration!')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, 'Username was logged out!')
    return redirect('login')


@login_required(login_url='login')
def user_account(request):
    prof = request.user.profiles
    skills = prof.skill_set.all()
    blogs = prof.blog_set.all()
    advertisement = prof.advertisement_set.all()
    context = {
        'profile': prof,
        'skills': skills,
        'blogs': blogs,
        'advertisement': advertisement,
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profiles
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def create_skill(request):
    profile = request.user.profiles
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')

            return redirect('account')

    context = {'form': form, 'title': 'Create'}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profiles
    skill = profile.skill_set.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully!')

        return redirect('account')

    context = {'skill': skill}
    return render(request, 'users/delete.html', context)


@login_required(login_url='login')
def update_skill(request, pk):
    profile = request.user.profiles
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')

            return redirect('account')

    context = {'form': form, 'title': 'Edit'}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profiles
    message_request = profile.messages.all()
    unread_count = message_request.filter(is_read=False).count()

    context = {
        "message_request": message_request,
        'unread_count': unread_count,
    }
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def view_message(request, pk):
    profile = request.user.profiles
    message = profile.messages.get(pk=pk)
    if not message.is_read:
        message.is_read = True
        message.save()

    context = {'message': message}
    return render(request, 'users/message.html', context)


def create_message(request, profile_pk):
    recipient = Profiles.objects.get(pk=profile_pk)
    form = MessageForm()
    sender = None
    if not request.user.is_authenticated:
        del form.fields['name']
        del form.fields['email']
        sender = request.user.profiles

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email

            messages.success(request, 'Your message is ok')
            message.save()

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/message-form.html', context)