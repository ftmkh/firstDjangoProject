from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect if user is already authenticated

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the user after signup
            return redirect('/')  # Redirect to home page after successful signup
        else:
            # If form is invalid, render the same page with error messages
            context = {'form': form}
            return render(request, 'accounts/signup.html', context)

    else:
        form = UserCreationForm()  # Create an empty form

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)



