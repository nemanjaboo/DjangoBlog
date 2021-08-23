from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .models import Profile

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # saving the user, hashes the password
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})


@login_required
def userpage(request):
    return render(request, 'users/userpage.html')

def profile(request, username):
    requser = get_object_or_404(User, username=username)
    requserposts = Post.objects.filter(author=requser)
    return render(request, 'users/profile.html', {'requser':requser, 'requserposts':requserposts})
