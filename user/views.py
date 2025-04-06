
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages  # Optional but useful for feedback

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Account created successfully! You can now log in.')  # Optional message
            return redirect('dashboard-index')  # Make sure this URL name exists in your urls.py
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


