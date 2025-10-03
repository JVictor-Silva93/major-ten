from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register():
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'login/register.html', {'form': form})

