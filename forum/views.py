from django.shortcuts import render, redirect 
from .models import Post 
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'forum/home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
        
    return render(request, 'forum/create_post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

