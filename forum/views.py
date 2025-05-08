from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Post 
from .forms import PostForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'forum/home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "your post has been shared")
            return redirect('home')
    else:
        form = PostForm()
        
    return render(request, 'forum/create_post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # only allow if user is also poster 
    if post.author != request.user:
        return HttpResponseForbidden("you can't delete someone else's post")
    
    if request.method == "POST":
        post.delete()
        messages.success(request, "your post has been deleted.")
        return redirect("home")

    return render(request, "forum/confirm_deletion.html", {"post": post})