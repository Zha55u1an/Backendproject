from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.images import ImageFile
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from .models import Category, Tag, Theme, Post, Comment

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'reviews/post_form.html', {'form': form})

def login(request):
    return render(request,'reviews/registration/login.html')

def logout(request):
    logout(request)
    return redirect('home')

def home_page(request):
    # Add your view logic here
    return render(request, 'reviews/home_page.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'reviews/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'reviews/post_detail.html', {'post': post})
def select_theme(request):
    themes = Theme.objects.all()
    return render(request, 'reviews/theme_select.html', {'themes': themes})

def customize_theme(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    if request.method == 'POST':
        form = ThemeCustomizationForm(request.POST, instance=theme)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    else:
        form = ThemeCustomizationForm(instance=theme)
        return render(request, 'reviews/theme_customize.html', {'form': form})
def post_comments(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post, approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'reviews/post_comments.html', {'post': post, 'comments': comments, 'form': form})
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'reviews/post_list.html', {'posts': posts})
