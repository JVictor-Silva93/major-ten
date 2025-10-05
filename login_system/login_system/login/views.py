from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('login:dashboard')

    else:
        form = RegistrationForm()

    return render(request, 'login/register.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get("remember_me")

        if not remember_me:
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(1209600)  # 2 weeks in seconds

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)

@login_required
def dashboard(request):
    return render(request, 'login/dashboard.html')
