from django.contrib import admin
from django.urls import path
from .views import register, CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/',register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]