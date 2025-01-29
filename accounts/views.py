
from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserModelForm, LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')  # Redirect to home or another page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')



def signup_view(request):
    if request.method == "POST":
        form = UserModelForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password1 = make_password(form.cleaned_data['password1'])
            user.password2 = make_password(form.cleaned_data['password2'])  # Optional, usually not needed
            user.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserModelForm()

    context = {
        "form":form,
    }

    return render(request, "accounts/signup.html" , context)
