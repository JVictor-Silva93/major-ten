from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, RegisterView, UserDetailView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,      # Built-in login view
    TokenRefreshView,         # Built-in token refresh view
)

app_name="login"

urlpatterns = [
    # JWT token endpoints (built-in from simplejwt)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Custom API endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserDetailView.as_view(), name='user_detail'),

    # path('register/', views.register, name='register'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]
