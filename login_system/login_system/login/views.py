from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer


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


class RegisterView(generics.CreateAPIView):
    """
    POST /api/register/
    Public endpoint - anyone can register.
    Returns JWT tokens upon successful registration.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)  # Don't require authentication
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate JWT tokens for the new user
        refresh = RefreshToken.for_user(user)

        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'User registered successfully'
        }, status=status.HTTP_201_CREATED)


class UserDetailView(generics.RetrieveAPIView):
    """
    GET /api/user/
    Protected endpoint - requires valid JWT token.
    Returns current user's information.
    """
    permission_classes = (IsAuthenticated,)  # Require valid JWT
    serializer_class = UserSerializer

    def get_object(self):
        # Returns the user from the JWT token
        return self.request.user
