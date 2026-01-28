from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    RefreshView,
    ChangePasswordView
)

urlpatterns = [
    path('auth/login/',LoginView.as_view(),name='login'),
    path('auth/logout/',LogoutView.as_view(),name='logout'),
    path('auth/refresh/',RefreshView.as_view(),name='login'),
    path('auth/Change-password/',ChangePasswordView.as_view(),name='login'),
      
]

