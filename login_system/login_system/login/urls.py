from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

app_name="login"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
