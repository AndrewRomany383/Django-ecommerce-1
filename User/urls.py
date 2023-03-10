from django.contrib import admin
from django.contrib.auth import views as authentication_view
from django.urls import path
from . import views

app_name = 'User'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', authentication_view.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', authentication_view.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('sellerprofile/<int:id>/', views.sellerprofile, name='sellerprofile'),
]






































