
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# from django.contrib import messages  # Optional but useful for feedback

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Account created successfully! You can now log in.')  # Optional message
            return redirect('user-login')  # Make sure this URL name exists in your urls.py
    else:
        form = CreateUserForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request,'user/profile.html')
