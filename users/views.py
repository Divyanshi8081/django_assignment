import hashlib
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Post
from .forms import RegisterForm, LoginForm, PostForm


def hash_password(raw):
    return hashlib.sha256(raw.encode()).hexdigest()


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        d = form.cleaned_data
        User.objects.create(
            first_name=d['first_name'], last_name=d['last_name'],
            email=d['email'], username=d['username'],
            password=hash_password(d['password']),
        )
        messages.success(request, 'Account created! Please log in.')
        return redirect('login')
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        d = form.cleaned_data
        try:
            user = User.objects.get(username=d['username'])
            if user.password == hash_password(d['password']):
                request.session['user_id']   = user.id
                request.session['username']  = user.username
                request.session['full_name'] = f"{user.first_name} {user.last_name}"
                messages.success(request, f'Welcome, {user.first_name}!')
                return redirect('create_post')
            messages.error(request, 'Incorrect password.')
        except User.DoesNotExist:
            messages.error(request, 'No user found with that username.')
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully.')
    return redirect('login')


def create_post_view(request):
    if not request.session.get('user_id'):
        messages.error(request, 'You must be logged in to create a post.')
        return redirect('login')
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        post      = form.save(commit=False)
        post.user = request.session['user_id']
        post.save()
        messages.success(request, 'Post published!')
        return redirect('create_post')
    posts = Post.objects.filter(user=request.session['user_id']).order_by('-created_at')
    return render(request, 'users/create_post.html', {'form': form, 'posts': posts})
